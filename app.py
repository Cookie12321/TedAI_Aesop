#!/usr/bin/env python3

from flask import Flask,request,render_template, url_for
from json import loads,dumps,load
from ai_test import test_openai, initialize_prompt_db, insert_into_prompt_db, view_prompts_db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
def home():
    test_openai()
    initialize_prompt_db()
    print("HELOOOOOOOOOOOOOOOO\n\n\n")
    return render_template('home.html')


@app.route('/robot_town', methods=['GET', 'POST'])
def openai():
    if request.method == "POST":
        p1 = request.form.get("prompt_1_answer")
        p2 = request.form.get("prompt_2_answer")
        p3 = request.form.get("prompt_3_answer")
        p4 = request.form.get("prompt_4_answer")
        p5 = request.form.get("prompt_5_answer")

        insert_into_prompt_db(p1+p2+p3+p4+p5)

        return f"Prompt answers: {p1}\n{p2}\n{p3}\n{p4}\n{p5} See database: http://localhost:8080/prompts_db"

    return render_template('robot_town.html')


@app.route('/prompts_db', methods=['GET'])
def prompts_db():
    return view_prompts_db()
