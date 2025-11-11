# coding=utf-8
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# JSON 데이터 불러오기
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# -------------------------------
# HTML 렌더링 (웹 페이지)
# -------------------------------

@app.route("/")
def index():
    return render_template("index.html", info=data)

@app.route("/subject")
def subject_page():
    return render_template("subject.html", info=data["subject"])

@app.route("/rationale")
def rationale_page():
    return render_template("rationale.html", info=data["rationale"])

@app.route("/features")
def features_page():
    return render_template("features.html", info=data["features"])

@app.route("/environment")
def environment_page():
    return render_template("environment.html", info=data["environment"])

@app.route("/team")
def team_page():
    return render_template("team.html", info=data["team"])

# -------------------------------
# API (요구사항 4: JSON 제공)
# -------------------------------
@app.get("/api/data")
def get_all_data():
    return jsonify(data)

@app.get("/api/subject")
def get_subject():
    return jsonify(data["subject"])

@app.get("/api/rationale")
def get_rationale():
    return jsonify(data["rationale"])

@app.get("/api/features")
def get_features():
    return jsonify(data["features"])

@app.get("/api/environment")
def get_environment():
    return jsonify(data["environment"])

@app.get("/api/team")
def get_team():
    return jsonify(data["team"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
