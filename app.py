#!/usr/bin/env python3

from flask import Flask,request,render_template, jsonify
from helper_functions import initialize_db, insert_to_prompts_table, view_prompts_table, view_scores_table, generate_story, psychoanalyze_prompt_responses
import json
from flask_cors import CORS

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    initialize_db()
    return render_template('home.html')


@app.route('/api/submit_exercise', methods=['POST'])
def processSubmission():
    try:
        data = request.get_json()
        AI_Prompt = json.dumps(data["responses"])
        story_name = data["conflict_name"]
        insert_to_prompts_table(story_name, AI_Prompt)
        generated_story = generate_story(AI_Prompt)
        SEL_scoring = psychoanalyze_prompt_responses(AI_Prompt)
        return {"generated_story": generated_story, "SEL_scoring": SEL_scoring}, 200 
        # return {"generated_story":["sample p1","sample p2", "sample p3", "sample p4", "sample p5", "sample p6", "sample p7", "sample p8"], "SEL_scoring":"sample SEL Scoring"}, 200
        
        return response
    except Exception as e:
        print(e)
        return {"message": "error"}, 500


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


@app.route('/api/get_scores', methods=['GET'])
def get_scores_from_db():
    try:
        return view_scores_table(), 200
    except Exception as e:
        return {"message": "error"}, 500
