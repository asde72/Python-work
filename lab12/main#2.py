class Team:
    def __init__(self):
        self.name ='none'
        self.wins = 0
        self.losses = 0
        self.percentage = 0

    def get_win_percentage(self, wins, losses):
        self.percentage = round((wins/losses),2)

    def print_standing(self):
        Team.get_win_percentage(self,user_wins,user_losses)
        if self.percentage > 0.5:
            self.average = "winning"
        else:
            self.average = "losing"
        print(f'Win percentage: {self.percentage}')
        print(f'Congratulations, Team {self.name} has a {self.average} average!')
        

if __name__ == "__main__":
    team = Team()
    user_name = input()
    user_wins = int(input())
    user_losses = int(input())
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    team.print_standing()
