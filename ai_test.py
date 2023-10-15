import openai
import sqlite3


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


def view_prompts_db():
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM prompt_results')
        return str(res.fetchall())