from flask import Blueprint, render_template, redirect, request
from models.match import Match
from models.team import Team
import repositories.matches_repository as matches_repository
import repositories.teams_repository as teams_repository

matches_blueprint = Blueprint("matches", __name__)

@matches_blueprint.route("/matches")
def matches():
    matches = matches_repository.select_all()
    teams = teams_repository.select_all()
    return render_template("matches/index.html", matches = matches, teams=teams)

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
    home_team_object = teams_repository.select(home_team)
    away_team_object = teams_repository.select(away_team)
    match = Match(home_team_object, away_team_object, home_score, away_score)
    matches_repository.save(match)
    return redirect('/matches')

@matches_blueprint.route("/matches/<id>/edit")
def edit_match(id):
    match = matches_repository.select(id)
    teams = teams_repository.select_all()
    return render_template("matches/edit.html", teams = teams, match = match)


@matches_blueprint.route("/matches/<id>/update", methods=['POST'])
def match_update(id):
    match = matches_repository.select(id)

    home_team = request.form['home_team']
    away_team = request.form['away_team']
    home_score = request.form['home_score']
    away_score = request.form['away_score']
    home_team_object = teams_repository.select(home_team)
    away_team_object = teams_repository.select(away_team)
    team = teams_repository.save(team.id)
    match.home_team = home_team_object
    match.away_team = away_team_object
    match.home_score= home_score
    match.away_score = away_score
    teams_repository.update(team)
    return redirect("/matches")

@matches_blueprint.route("/matches/<id>/delete", methods=['POST'])
def delete_match(id):
    matches_repository.delete(id)
    return redirect('/matches')