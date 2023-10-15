#!/usr/bin/env python3

from flask import Flask,request,render_template
from ai_test import initialize_prompt_db, insert_into_prompt_db, view_prompts_db, open_ai_real

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
def home():
    initialize_prompt_db()
    return render_template('home.html')


@app.route('/robot_town', methods=['GET', 'POST'])
def robot_town():
    if request.method == "POST":
        p1 = request.form.get("prompt_1_answer")
        p2 = request.form.get("prompt_2_answer")
        p3 = request.form.get("prompt_3_answer")
        p4 = request.form.get("prompt_4_answer")
        p5 = request.form.get("prompt_5_answer")
        insert_into_prompt_db("robot_town", p1+p2+p3+p4+p5)
        res = open_ai_real(p1+p2+p3+p4+p5)
        return f"Prompt answer analysis: {res} See database: http://localhost:8080/prompts_db"

    return render_template('robot_town.html')


@app.route('/enchanted_jungle', methods=['GET', 'POST'])
def enchanted_jungle():
    if request.method == "POST":
        p1 = request.form.get("prompt_1_answer")
        p2 = request.form.get("prompt_2_answer")
        p3 = request.form.get("prompt_3_answer")
        p4 = request.form.get("prompt_4_answer")
        p5 = request.form.get("prompt_5_answer")
        insert_into_prompt_db("enchanted_jungle", p1+p2+p3+p4+p5)
        res = open_ai_real(p1+p2+p3+p4+p5)
        return f"Prompt answer analysis: {res} See database: http://localhost:8080/prompts_db"

    return render_template('enchanted_jungle.html')


@app.route('/prompts_db', methods=['GET'])
def prompts_db():
    return view_prompts_db()
