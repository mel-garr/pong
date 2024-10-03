
from ..models import *
from . import *
from .player import Player


class Game:
    def __init__(self, room):
        self.name = room.name
        self.gamestatus = room.gamestatus
        self.gametype = room.gametype
        self.redteamplayers = self.initteam(room.redteamplayers)
        self.blueteamplayers = self.initteam(room.blueteamplayers, side='blue')
        

    def initteam(self, team, side='red'):
        squad = []
        i = 1
        for teamp in team.all():
            tp = Player(teamp, i, side)
            squad.append(tp)
            i += 1
        return squad

    def start_game(self):
        print ('AAAA')
