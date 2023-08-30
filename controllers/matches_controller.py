from flask import Blueprint, render_template, redirect, request
from models.match import Match
from models.team import Team
import repositories.matches_repository as matches_repository
import repositories.teams_repository as teams_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = matches_repository.select_all()
    return render_template("matches/index.html", matches = matches)

@matches_blueprint.route("/matches/<id>")
def show(id):
    match = matches_repository.select(id)
    teams = teams_repository.teams_by_match(match)
    return render_template("matches/show.html", match=match, teams=teams)

@matches_blueprint.route("/matches/new", methods=['GET'])
def new_match():
    teams = teams_repository.select_all()
    matches = matches_repository.select_all()
    return render_template("matches/show.html", teams = teams, matches = matches)

@matches_blueprint.route("/matches",  methods=['POST'])
def create_match():
    home_team = request.form['home_team']
    away_team = request.form['away_team']
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    match = Match(home_team, away_team, home_score, away_score, id)
    matches_repository.save(match)
    return redirect('/matches')

@matches_blueprint.route("/matches/<id>/update", methods=['POST'])
def match_update():
    home_team = request.form['home_team']
    away_team = request.form['away_team']
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    team = teams_repository.save(team.id)
    match = Match(home_team, away_team, home_score, away_score, id)
    return redirect("/matches")

@matches_blueprint.route("/matches/<id>/delete", methods=['POST'])
def delete_match(id):
    matches_repository.delete(id)
    return redirect('/matches')
