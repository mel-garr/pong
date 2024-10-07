
from ..models import *
from . import *
from .player import Player
import random
from asgiref.sync import sync_to_async


class Game:
    def __init__(self, room):
        self.name = room.name
        self.gamestatus = room.gamestatus
        self.gametype = room.gametype
        self.winningteam = room.winning_team
        self.max_score = room.max_score

        #
        self.ballside = None
        self.playplayer = None
        

        #init data of each team
        self.redteamplayers = None
        self.redteamball =  None
        self.redfield = None
        self.redscore = 0

        self.blueteamplayers = None
        self.blueteamball = None
        self.bluefield = None
        self.bluescore = 0

        
    async def initialize_game(self, room):
        self.redteamplayers = await self.initteam(room.redteamplayers)
        self.blueteamplayers = await self.initteam(room.blueteamplayers, side='blue')

        self.redteamball = await self.getball(self.redteamplayers)
        self.redfield = await self.getfield(self.redteamplayers)
        self.blueteamball = await self.getball(self.blueteamplayers)
        self.bluefield = await self.getfield(self.blueteamplayers)
        
        self.ballside = await self.getballside()  
        self.playplayer = await self.getpauseplayer()

    async def initteam(self, team, side='red'):
        squad = []
        i = 1
        team_list = await sync_to_async(list)(team.all())
        for teamp in team_list:
            tp = Player(teamp, i, side)
            squad.append(tp)
            i += 1
        return squad

    async def getpauseplayer(self):
        return self.ballside.side

    async def getball(self, team):
        avatar = random.choice(list(team)) if team else None
        return avatar.ball if avatar else None

    async def getfield(self, team):
        avatar = random.choice(list(team)) if team else None
        return avatar.field if avatar else None
    
    async def getballside(self):
        return random.choice([self.redteamball, self.blueteamball])

    def start_game(self):
        print ('AAAA')
        print ('game_statue: ', self.gamestatus)

        # print (update)
        #     print ('ja hna:', teamgs)

    def is_player_in(self, pl_name, teamplayers):
        return any(pl.name == pl_name for pl in teamplayers)

    async def updategame(self, update):
        print ('play_statue: ', self.playplayer)
        print ('after change:' ,self.gamestatus)
        if self.gamestatus == 'pause':
            teamgs = self.blueteamplayers if self.playplayer == 'blue' else self.redteamplayers
            for k in update:
                if k['action'] == 'gs':
                    if self.is_player_in(k['player'], teamgs):
                        self.gamestatus = 'gamestart'
                        return

        if self.gamestatus == 'gamestart':
            if any(gss['action'] == 'gs' for gss in update):
                for gss in update:
                    if gss['action'] == 'gs':
                        self.gamestatus= 'pause'
                        self.playplayer = 'blue' if self.is_player_in(gss['player'], self.blueteamplayers) else 'red'
                        print (self.playplayer)
                        return


        #     pass
            #updtae status
            #update player
            #update ball
        


    def serialize_game_data(self):
        return {
            'redteamplayers' : [player.serialize() for player in self.redteamplayers],
            'blueteamplayers': [player.serialize() for player in self.blueteamplayers],
            'name'           : self.name,
            'status'         : self.gamestatus,
            'gametype'       : self.gametype,
            'winningteam'    : self.winningteam,
            'max_score'      : self.max_score,
            'ballside'       : (self.ballside).serialize(),
            # 'redteamball'    : (self.redteamball).serialize(),
            'redfield'       : (self.redfield).serialize(),
            'redscore'       : self.redscore,
            # 'blueteamball'   : (self.blueteamball).serialize(),
            'bluefield'      : (self.bluefield).serialize(),
            'bluescore'      : self.bluescore,
        }
