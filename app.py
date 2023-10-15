#!/usr/bin/env python3

from flask import Flask,request,render_template
from helper_functions import initialize_db, insert_to_prompts_table, view_prompts_table, view_scores_table, generate_story, psychoanalyze_prompt_responses

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET'])
def home():
    initialize_db()
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
        insert_to_prompts_table("missing_parts", p1 + p2 + p3 + p4 + p5)
        story = generate_story(q1 + p1 + q2 + p2 + q3 + p3 + q4 + p4 + q5 + p5)
        scores = psychoanalyze_prompt_responses(p1 + p2 + p3 + p4 +p5)
        return f"{story}<br><br>Prompt answer analysis: {scores}<br><br>See prompts database: http://localhost:8080/get_prompt_results<br><br>See scores database:http://localhost:8080/get_scores"

    return render_template('missing_parts.html')


@app.route('/broken_bridge', methods=['GET', 'POST'])
def broken_bridge():
    if request.method == "POST":
        q1 = "What happens to the bridge in Robot Town that connects two important parts of the town, making it impossible for the robots to get from one side to the other?"
        q2 = "How do the robots react when they realize they can't cross the bridge?"
        q3 = "What do the robots do to try to fix the bridge?"
        q4 = "What do the robots do when they find out who broke the bridge?"
        q5 = "How do the robots ultimately fix the bridge, and what do they learn from this experience?"

        p1 = request.form.get("prompt_1_answer")
        p2 = request.form.get("prompt_2_answer")
        p3 = request.form.get("prompt_3_answer")
        p4 = request.form.get("prompt_4_answer")
        p5 = request.form.get("prompt_5_answer")
        insert_to_prompts_table("broken_bridge", p1 + p2 + p3 + p4 + p5)
        story = generate_story(q1 + p1 + q2 + p2 + q3 + p3 + q4 + p4 + q5 + p5)
        scores = psychoanalyze_prompt_responses(p1 + p2 + p3 + p4 + p5)
        return f"{story}<br><br>Prompt answer analysis: {scores}<br><br>See prompts database: http://localhost:8080/get_prompt_results<br><br>See scores database:http://localhost:8080/get_scores"

    return render_template('broken_bridge.html')


@app.route('/get_prompt_results', methods=['GET'])
def get_prompt_results_from_db():
    return view_prompts_table()


@app.route('/get_scores', methods=['GET'])
def get_scores_from_db():
    return view_scores_table()
