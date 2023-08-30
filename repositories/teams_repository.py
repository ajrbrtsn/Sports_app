from db.run_sql import run_sql
from models.team import Team
import pdb

def save(team):
    sql = "INSERT INTO teams (name, stadium) VALUES (%s, %s) RETURNING id"
    values = [team.name, team.stadium]
    results = run_sql (sql, values)
    team.id = results[0]['id']
    return team

def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['name'], row['stadium'], row['id'])
        teams.append(team)
    return teams

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        team = Team(result['name'], result['stadium'], result['id'])
    return team

def update(team):
    sql = "UPDATE teams SET (name, stadium) = (%s, %s) WHERE id = %s"
    values = [team.name, team.stadium, team.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)