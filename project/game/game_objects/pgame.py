
from ..models import *
from . import *
from .player import Player
import random

class Game:
    def __init__(self, room):
        self.name = room.name
        self.gamestatus = room.gamestatus
        self.gametype = room.gametype
        self.winningteam = room.winning_team
        self.max_score = room.max_score
        self.ballside = self.getballside()

        #init data of each team
        self.redteamplayers = self.initteam(room.redteamplayers)
        self.redteamball = self.getball(self.redteamplayers)
        self.redfield = self.getfield(self.redteamplayers)
        self.redscore = 0

        self.blueteamplayers = self.initteam(room.blueteamplayers, side='blue')
        self.blueteamball = self.getball(self.blueteamplayers)
        self.bluefield = self.getfield(self.blueteamplayers)
        self.bluescore = 0

        

    def initteam(self, team, side='red'):
        squad = []
        i = 1
        for teamp in team.all():
            tp = Player(teamp, i, side)
            squad.append(tp)
            i += 1
        return squad


    def getball(self, team):
        avatar = random.choice(list(team)) if team else None
        return avatar.ball

    def getfield(self, team):
        avatar = random.choice(list(team)) if team else None
        print (avatar.field.color)
        return avatar.field
    
    def getballside(self):
        return random.choice(['blue', 'red'])

    def start_game(self):
        print ('AAAA')
