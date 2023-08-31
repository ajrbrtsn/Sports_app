from db.run_sql import run_sql
from models.match import Match
from models.team import Team
from repositories import teams_repository
from repositories import matches_repository

def save(match):
    sql = "INSERT INTO matches ( home_team, away_team, home_score, away_score) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [match.home_team.id, match.away_team.id, match.home_score, match.away_score]
    results = run_sql( sql, values )
    match.id = results[0]['id']
    return match

def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        home_team = teams_repository.select(row['home_team'])
        away_team = teams_repository.select(row['away_team'])
        match = Match(home_team, away_team, row['home_score'], row['away_score'], row['id'])
        matches.append(match)
    return matches

def select(id):
    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        match = Match(result['home_team'], result['away_team'], result['home_score'], result['away_score'], result['id'])
    return match

def update(match):
    sql = "UPDATE matches SET (home_team, away_team, home_score, away_score) = (%s, %s, %s, %s) WHERE id = %s"
    values = [match.home_team.id, match.away_team.id, match.home_score, match.away_score]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def matchbyteam(team):
    matches=[]
    sql = "SELECT * FROM matches WHERE home_team= %s OR away_team = %s"
    values = [team.id,team.id]
    results = run_sql(sql, values)
    for row in results:
        home_team = teams_repository.select(row['home_team'])
        away_team = teams_repository.select(row['away_team'])
        match = Match(home_team, away_team, row['home_score'], row['away_score'], row['id'])
        matches.append(match)
    return matches