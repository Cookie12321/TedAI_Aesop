#!/usr/bin/env python3

from flask import Flask,request,render_template
from ai_test import initialize_prompt_db, insert_into_prompt_db, view_prompts_db, psychoanalyze_prompt_responses

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
def home():
    initialize_prompt_db()
    return render_template('home.html')


@app.route('/missing_parts', methods=['GET', 'POST'])
def missing_parts():
    if request.method == "POST":
        q1 = "What starts happening in Robot Town that makes the robots realize some of their essential robot parts are disappearing?"
        q2 = "How do the robots feel when they discover that their parts are missing?"
        q3 = "What do the robots do to try to find their missing parts?"
        q4 = "What do the robots do when they find out who is taking their parts?"
        q5 = "How do the robots ultimately recover their missing parts, and what do they learn from this experience?"

        p1 = request.form.get("prompt_1_answer")
        p2 = request.form.get("prompt_2_answer")
        p3 = request.form.get("prompt_3_answer")
        p4 = request.form.get("prompt_4_answer")
        p5 = request.form.get("prompt_5_answer")
        insert_into_prompt_db("missing_parts", p1 + p2 + p3 + p4 + p5)
        res = psychoanalyze_prompt_responses(p1 + p2 + p3 + p4 +p5)
        return f"Prompt answer analysis: {res} See database: http://localhost:8080/prompts_db"

    return render_template('missing_parts.html')


@app.route('/broken_bridge', methods=['GET', 'POST'])
def broken_bridge():
    if request.method == "POST":
        p1 = request.form.get("prompt_1_answer")
        p2 = request.form.get("prompt_2_answer")
        p3 = request.form.get("prompt_3_answer")
        p4 = request.form.get("prompt_4_answer")
        p5 = request.form.get("prompt_5_answer")
        insert_into_prompt_db("broken_bridge", p1 + p2 + p3 + p4 + p5)
        res = psychoanalyze_prompt_responses(p1 + p2 + p3 + p4 + p5)
        return f"Prompt answer analysis: {res} See database: http://localhost:8080/prompts_db"

    return render_template('broken_bridge.html')


@app.route('/prompts_db', methods=['GET'])
def prompts_db():
    return view_prompts_db()
