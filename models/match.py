class Match:

    def __init__(self, home_team, away_team, home_score, away_score, id = None ):
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score
        self.id = id
    
    def winner(self):
        if self.home_score > self.away_score:
            return self.home_team
        elif self.away_score > self.home_score:
            return self.away.score
        else:
            return "Draw"
        



    
