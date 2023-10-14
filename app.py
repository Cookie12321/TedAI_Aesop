#!/usr/bin/env python3

from flask import Flask,request,render_template, url_for
from json import loads,dumps,load
from ai_test import test_openai, test_sqlite3

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
def home():
    test_openai()
    test_sqlite3()
    print("HELOOOOOOOOOOOOOOOO\n\n\n")
    return render_template('home.html')


@app.route('/robot_town', methods=['GET', 'POST'])
def openai():
    if request.method == "POST":
        prompt_1_answer = request.form.get("prompt_1_answer")
        prompt_2_answer = request.form.get("prompt_2_answer")
        prompt_3_answer = request.form.get("prompt_3_answer")
        prompt_4_answer = request.form.get("prompt_4_answer")
        prompt_5_answer = request.form.get("prompt_5_answer")

        return f"Prompt answers: {prompt_1_answer}\n{prompt_2_answer}\n{prompt_3_answer}\n{prompt_4_answer}\n{prompt_5_answer}"

    return render_template('robot_town.html')
