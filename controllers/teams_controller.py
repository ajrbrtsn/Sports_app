from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
# from models.match import Match
from repositories import teams_repository
from repositories import matches_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route('/teams')
def teams():
    teams = teams_repository.select_all()
    matches = matches_repository.select_all()
    print(matches)
    return render_template("teams/index.html", teams = teams, matches=matches)

@teams_blueprint.route("/teams/<id>")
def show(id):
    team = teams_repository.select(id)
    matches = matches_repository.select_all()(team)
    return render_template("teams/show.html", team=team, matches=matches)

@teams_blueprint.route("/teams/new", methods=['GET'])
def new_team():
    teams = teams_repository.select_all()
    matches = matches_repository.select_all()
    return render_template("teams/show.html", teams = teams, matches = matches)

@teams_blueprint.route("/teams",  methods=['POST'])
def create_team():
    name = request.form['name']
    stadium = request.form['stadium']
    id = request.form['id']
    teams = teams_repository.select(teams.id)
    match = matches_repository.select(match.id)
    team = Team(name, stadium, id)
    teams_repository.save(team)
    return redirect('/teams')

@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    teams_repository.delete(id)
    return redirect('/team')