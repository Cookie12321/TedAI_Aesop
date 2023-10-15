#!/usr/bin/env python3

from flask import Flask,request,render_template, url_for
from json import loads,dumps,load
from ai_test import test_openai, test_sqlite3, open_ai_real

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
        p1 = request.form.get("prompt_1_answer")
        p2 = request.form.get("prompt_2_answer")
        p3 = request.form.get("prompt_3_answer")
        p4 = request.form.get("prompt_4_answer")
        p5 = request.form.get("prompt_5_answer")

        res = open_ai_real(p1+p2+p3+p4+p5)
        return f"Prompt answer analysis: {res}"

    return render_template('robot_town.html')
