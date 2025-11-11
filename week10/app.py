# coding=utf-8
from flask import Flask, render_template, Response
import json

app = Flask(__name__)

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
# JSON 응답 헬퍼
# -------------------------------
def json_response(obj):
    return Response(
        json.dumps(obj, ensure_ascii=False),
        mimetype="application/json; charset=utf-8"
    )

# -------------------------------
# API (JSON 제공)
# -------------------------------
@app.get("/api/data")
def get_all_data():
    return json_response(data)

@app.get("/api/subject")
def get_subject():
    return json_response(data["subject"])

@app.get("/api/rationale")
def get_rationale():
    return json_response(data["rationale"])

@app.get("/api/features")
def get_features():
    return json_response(data["features"])

@app.get("/api/environment")
def get_environment():
    return json_response(data["environment"])

@app.get("/api/team")
def get_team():
    return json_response(data["team"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
