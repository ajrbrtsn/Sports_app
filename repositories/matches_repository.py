from db.run_sql import run_sql
from models.match import Match

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
        match = Match(row['home_team'], row['away_team'], row['home_score'], row['away_score'], row['id'])
        matches.append(match)
    return matches

def select(id):
    user = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

def update(match):
    sql = "UPDATE matches SET (home_team, away_team, home_score, away_score) = (%s, %s, %s, %s) WHERE id = %s"
    values = [match.home_team, match.away_team, match.home_score, match.away_score]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM matches"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)