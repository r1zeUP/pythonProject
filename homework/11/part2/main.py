from flask import Flask, render_template
from tools import get_all_candidate, get_candidate, get_candidates_by_name, get_candidates_by_skill
app = Flask(__name__)


@app.route("/")
def index():
    candidates = get_all_candidate()
    return render_template("listе.html", candidates=candidates)


@app.route("/candidates/<int:id>")
def get_candidate_by_id(id):
    candidate = get_candidate(id)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidate_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, count_candidates=len(candidates))


@app.route("/skill/<skill>")
def get_candidate_by_skill(skill):
    candidates = get_candidates_by_skill(skill)
    return render_template("skill.html", candidates=candidates, count_candidates=len(candidates))


app.run(debug=True)
