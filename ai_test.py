import openai
import sqlite3


def test_openai():
    openai.api_key = ""
    print("open ai hehe")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Tell me about the covid 19.",
        max_tokens=60,
    )
    print(response)


def test_sqlite3():
    with sqlite3.connect('mydb.sqlite') as conn:
        cur = conn.cursor()
        cur.execute("drop table if exists users")
        cur.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
        cur.execute('INSERT INTO users (name) VALUES (?)', ('John Doe',))
        conn.commit()

        res = cur.execute('SELECT * FROM users')
        print("SQLITE3 HEHEHHEE:")
        print(res.fetchone())