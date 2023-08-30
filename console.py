import pdb
from models.team import Team
from models.match import Match

from repositories import teams_repository
from repositories import matches_repository

teams_repository.delete_all()
matches_repository.delete_all()

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

match3 = Match(team_1, team_3, 3, 1 )
matches_repository.save(match3)

match4 = Match(team_2, team_4, 1, 1 )
matches_repository.save(match4)

results = teams_repository.select_all()
pdb.set_trace()