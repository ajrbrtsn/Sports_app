from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
from repositories import teams_repository
from repositories import matches_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route('/teams')
def teams():
    teams = teams_repository.select_all()
    matches = matches_repository.select_all()
    print(matches)
    return render_template("teams/index.html", teams=teams, matches=matches)

@teams_blueprint.route("/teams/<id>")
def show(id):
    team = teams_repository.select(id)
    matches = matches_repository.matchbyteam(team)
    return render_template("teams/show.html", team=team, matches=matches)

@teams_blueprint.route("/teams/new", methods=['GET'])
def new_team():
    teams = teams_repository.select_all()
    matches = matches_repository.select_all()
    return render_template("teams/show.html", teams=teams, matches=matches)

@teams_blueprint.route("/teams",  methods=['POST'])
def create_team():
    name = request.form['name']
    stadium = request.form['stadium']
    team = Team(name, stadium)
    teams_repository.save(team)
    return redirect('/teams')

@teams_blueprint.route("/teams/<id>/edit", methods=['GET'])
def edit_team(id):
    team = teams_repository.select(id)
    return render_template("teams/edit.html", team=team)

@teams_blueprint.route("/teams/<id>/update", methods=['POST'])
def team_update(id):
    name = request.form['name']
    stadium = request.form['stadium']
    team = teams_repository.select(id)
    team.name = name
    team.stadium = stadium
    teams_repository.update(team)
    return redirect("/teams")

@teams_blueprint.route("/teams/<id>/delete", methods=['POST'])
def delete_team(id):
    teams_repository.delete(id)
    return redirect('/teams')