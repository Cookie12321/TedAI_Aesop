import openai
import sqlite3
import json


API_KEY = "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"


def initialize_db():
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        cur.execute("drop table if exists prompt_results")
        cur.execute('create table prompt_results (id integer primary key, category text, prompt_answers text)')
        cur.execute("drop table if exists scorsg_scores")
        cur.execute('create table scorsg_scores (com tinyint, aff tinyint, eir tinyint, eim tinyint, sc tinyint, agg tinyint, se tinyint, ics tinyint, insert_ts timestamp default current_timestamp)')
        conn.commit()


def insert_to_prompts_table(category, prompt_answers):
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        cur.execute(f"insert into prompt_results (category, prompt_answers) values ('{category}', '{prompt_answers}')")
        conn.commit()

    
def insert_to_scores_table(scoring):
        json_scores = json.loads(scoring)
        scores = {}
        scores["com"] = json_scores["COM"]["score"]
        scores["aff"] = json_scores["AFF"]["score"]
        scores["eir"] = json_scores["EIR"]["score"]
        scores["eim"] = json_scores["EIM"]["score"]
        scores["sc"] = json_scores["SC"]["score"]
        scores["agg"] = json_scores["AGG"]["score"]
        scores["se"] = json_scores["SE"]["score"]
        scores["ics"] = json_scores["ICS"]["score"]

        with sqlite3.connect('mydb.sqlite') as conn:
            cur = conn.cursor()
            cur.execute(f"insert into scorsg_scores (com, aff, eir, eim, sc, agg, se, ics) values ({scores['com']},{scores['aff']},{scores['eir']},{scores['eim']},{scores['sc']},{scores['agg']},{scores['se']},{scores['ics']})")
            conn.commit()


def view_prompts_table():
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        res = cur.execute('select * from prompt_results')
        return res.fetchall()
    

def view_scores_table(limit=20):
    final_json = {}
    final_json["COM"] = []
    final_json["AFF"] = []
    final_json["EIR"] = []
    final_json["EIM"] = []
    final_json["SC"] = []
    final_json["AGG"] = []
    final_json["SE"] = []
    final_json["ICS"] = []
    
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        res = cur.execute(f'select com, aff, eir, eim, sc, agg, se, ics from scorsg_scores order by insert_ts asc limit {limit}')
        results = res.fetchall()
        
        for row in results:
            final_json["COM"].append(row[0])
            final_json["AFF"].append(row[1])
            final_json["EIR"].append(row[2])
            final_json["EIM"].append(row[3])
            final_json["SC"].append(row[4])
            final_json["AGG"].append(row[5])
            final_json["SE"].append(row[6])
            final_json["ICS"].append(row[7])

    return final_json
        

def generate_story(combined_prompts_and_answers):
    openai.api_key = API_KEY
    chat_completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo', 
        messages=[
            {
                'role': 'system',
                'content': 'Write a story between 300 and 400 words based on the user\'s answers to the prompt questions.'
            },
            {
                'role': 'user'
                ,'content': combined_prompts_and_answers
            },
        ]
    )

    story = chat_completion["choices"][0]["message"]["content"]
    end_character = (".", "!", "?")
    book = []
    current_page = ""
    end_char_count = 0

    for char in story:
        current_page += char
        if char in end_character:
            end_char_count += 1
            if end_char_count % 3 == 0:
                book.append(current_page.replace("\n\n", " ").strip())
                current_page = ""

    if current_page != "":
        book.append(current_page.replace("\n\n", " ").strip())
    return book
    

def psychoanalyze_prompt_responses(combined_prompt_answers):
    openai.api_key = API_KEY
    with open('./scoring_criteria.json', "r") as f:
        scoring_criteria = json.load(f)
    with open('./response_example.json', "r") as f:
        response_example = json.load(f)
        
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {
                'role': 'system',
                'content': f'score user responses based on : {json.dumps(scoring_criteria)}. Respond in json format like this: {json.dumps(response_example)}. Irrelevant or not understandable responses get a 4, and a description of "not applicable"'},
            {
                'role': 'user',
                'content': combined_prompt_answers
            }
        ]
    )
    scoring = chat_completion['choices'][0]['message']['content']
    insert_to_scores_table(scoring)
    return scoring
