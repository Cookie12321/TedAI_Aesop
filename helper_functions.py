import openai
import sqlite3
import json


API_KEY = ""


def initialize_prompt_db():
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        cur.execute("drop table if exists prompt_results")
        cur.execute('create table prompt_results (id integer primary key, category text, prompt_answers text)')
        conn.commit()


def insert_into_prompt_db(category, prompt_answers):
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        cur.execute(f"insert into prompt_results (category, prompt_answers) values ('{category}', '{prompt_answers}')")
        conn.commit()


def view_prompts_db():
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        res = cur.execute('select * from prompt_results')
        return res.fetchall()
        

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
    return story
    

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
    return scoring
