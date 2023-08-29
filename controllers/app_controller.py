from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
from models.match import Match
from repositories import teams_repository
from repositories import matches_repository

teams_blueprint = Blueprint("teams", __name__)

@teams_blueprint.route('/teams')
def teams():
    teams = teams_repository.select_all()
    return render_template("teams/index.html", all_teams = teams)

