#!/usr/bin/env python3

from flask import Flask,request,render_template, url_for
from json import loads,dumps,load
from ai_test import test_openai

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
def home():
    test_openai()
    print("HELOOOOOOOOOOOOOOOO\n\n\n")
    return render_template('home.html')


@app.route('/robot_town', methods=['GET', 'POST'])
def openai():
    if request.method == "POST":
        fname = request.form.get("fname")
        lname = request.form.get("lname") 

        return "Your name is "+ fname + lname

    return render_template('openai.html')
