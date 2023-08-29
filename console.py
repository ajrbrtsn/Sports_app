import pdb
from models.team import Team
from models.match import Match

from repositories import teams_repository
from repositories import matches_repository

team_1 = Team("Scotland", "Hampden")
teams_repository.save(team_1)

team_2 = Team("England", "Wembley")
teams_repository.save(team_2)

team_3 = Team("Wales", "Millennium Stadium")
teams_repository.save(team_3)

team_4 = Team("Northern Ireland", "Windsor Park")
teams_repository.save(team_4)

match1 = Match(team_1, team_2, 2, 0 )
matches_repository.save(match1)

match2 = Match(team_3, team_4, 2, 5 )
matches_repository.save(match2)

match3 = Match(team_1, team_3, 1, 1 )
matches_repository.save(match3)

results = teams_repository.select_all()
pdb.set_trace()