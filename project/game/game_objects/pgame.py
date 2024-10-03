
from ..models import *
from . import *


class Game:
    def __init__(self, room):
        self.name = room.name
        self.gamestatus = room.gamestatus
        self.gametype = room.gametype
        self.redteamplayers = initteam(room.redteamplayers)
        self.blueteamplayers = initteam(room.blueteamplayers, side='blue')
        

    def initteam(team, side='red'):
        squad = []
        i = 1
        for teamp in team:
            tp = Player(teamp, side, i)
            squad.append(tp)
            i += 1
        return squad

    def start_game(self):
        print ('AAAA')
