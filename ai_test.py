import openai
import sqlite3
import json
from flask import jsonify

def test_openai():
    openai.api_key = ""
    print("open ai hehe")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Tell me about iphones.",
        max_tokens=60,
    )
    print(response)


def initialize_prompt_db():
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        cur.execute("drop table if exists prompt_results")
        cur.execute('create table prompt_results (id INTEGER PRIMARY KEY, prompt_answers TEXT)')
        conn.commit()


def insert_into_prompt_db(prompt_answers):
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO prompt_results (prompt_answers) VALUES (?)', (f'{prompt_answers}',))
        conn.commit()

        res = cur.execute('SELECT * FROM users')
        print("SQLITE3 HEHEHHEE:")
        print(res.fetchone())
        
def open_ai_real(big_prompt_string):
    openai.api_key = ""
    with open('./scoring_criteria.json','r') as f:
        scoring_criteria = json.load(f)
    with open('./response_example.json','r') as f:
        response_example = json.load(f)
        
    chat_completion = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role':'system','content':f'score user responses based on : {json.dumps(scoring_criteria)}. Respond in json format like this:{json.dumps(response_example)}. Irrelevant or not understandable responses get a 4, and a description of "not applicable"'},{'role':'user','content':big_prompt_string}])
    result_json = chat_completion['choices'][0]['message']['content']
    

    print(result_json)
    return result_json