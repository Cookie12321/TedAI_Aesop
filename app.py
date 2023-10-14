#!/usr/bin/env python3

from flask import Flask,request,render_template
from json import loads,dumps,load
import openai

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# @app.route('/')
# def hello():
#     if 'use_template' in request.args:
#         return render_template('hello.html')
#     else:
#         return 'Hello World!fdsaf'

@app.route('/', methods=['GET', 'POST'])
def openai():
    return render_template('openai.html')