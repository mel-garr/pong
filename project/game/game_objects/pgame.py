
from ..models import *
from . import *
from .player import Player
from .powerup import Powerup
import random
from asgiref.sync import sync_to_async
import time
import asyncio

class Game:
    def __init__(self, room):
        self.name = room.name
        self.gamestatus = room.gamestatus
        self.gametype = room.gametype
        self.winningteam = room.winning_team
        # self.max_score = room.max_score
        self.max_score = 1


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

        #gameplay
        self.game_objects = []
        self.game_balls = []
        self.lastpowerup = None
        self.powerup_task = None
        self.working_on_pp = 0
        #add so;ething to hold balls and multiple balls
        #what avout ndir wahed taystori hir lbalss ou wa7ed akhour taystori bonuses
        
    async def initialize_game(self, room):
        self.redteamplayers = await self.initteam(room.redteamplayers)
        self.blueteamplayers = await self.initteam(room.blueteamplayers, side='blue')

        self.redteamball = await self.getball(self.redteamplayers)
        self.redfield = await self.getfield(self.redteamplayers)
        self.blueteamball = await self.getball(self.blueteamplayers)
        self.bluefield = await self.getfield(self.blueteamplayers)
        
        self.ballside = await self.getballside()
        # self.pa self.getpauseplayer()
        # self.game_balls.append(self.ballside)

        self.lastpowerup = time.time()

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

                

        self.gamestatus = 'pause'
        new_ball = await self.redteamball.clone() if self.redscore < self.bluescore else await self.blueteamball.clone() if self.redscore > self.bluescore else random.choice([await self.redteamball.clone(), await self.blueteamball.clone()])
        self.playplayer = new_ball.side
        # self.playplayer = await self.getpauseplayer()
        self.game_balls.append(new_ball)
        if self.redscore >= self.max_score or self.bluescore >= self.max_score:
            self.gamestatus = 'ended'
        # return new_ball

    def start_game(self):
        print ('AAAA')
        print ('game_statue: ', self.gamestatus)



    def is_player_in(self, pl_name, teamplayers):
        return any(pl.name == pl_name for pl in teamplayers)


    async def updateGameState(self, update):
        if self.gamestatus == 'pause':
            teamgs = self.blueteamplayers if self.playplayer == 'blue' else self.redteamplayers
            for k in update:
                if k['action'] == 'gs':
                    if self.is_player_in(k['player'], teamgs):
                        self.gamestatus = 'gamestart'
                        return 0

        if self.gamestatus == 'gamestart':
            if any(gss['action'] == 'gs' for gss in update):
                for gss in update:
                    if gss['action'] == 'gs':
                        self.gamestatus= 'pause'
                        self.playplayer = 'blue' if self.is_player_in(gss['player'], self.blueteamplayers) else 'red'
                        return 0
        return 1
        

    async def witch_player(self, name):
        for player in self.redteamplayers:
            if player.name == name:
                return player

        for player in self.blueteamplayers:
            if player.name == name:
                return player
        print ('error witchplayer')
        return (None)

    async def reset_new_ball(self):
        #reset game status
        #generate new ball depending on the player with lower score ,
        pass

    # async def spawn_powerup(self):
    #     print ('16')
    #     while self.gamestatus == 'gamestart':
    #         await asyncio.sleep(5)
    #         power = Powerup()
    #         print ('ja lspawn')
    #         print (len( self.game_objects.append))

    #         self.game_objects.append(power)
    #         print (len( self.game_objects.append))
    #         exit()

    async def drop_bonus(self):
        if self.gamestatus == 'gamestart' and not self.working_on_pp and len(self.game_objects) < 3:
            self.working_on_pp = 1
            await asyncio.sleep(4)
            powerup = Powerup()
            self.game_objects.append(powerup)
            self.working_on_pp = 0
        # pass


    async def reset_ball(self):
        if self.gamestatus == 'gamestart':
            # print('jit hnaya 2')
            await self.getballside()

    async def updateball(self):
        # print ('gamestatus mn updateballl: ', self.gamestatus)
        if self.redscore >= self.max_score or self.bluescore >= self.max_score:
                print ('game_salat: ', self.game_status)
                self.winningteam = 'Red Won' if self.redscore > self.max_score else 'BLue Won'
                self.gamestatus == 'ended'
        if self.gamestatus == 'gamestart':
            
            for player in self.blueteamplayers:
                await player.paddle.checkcolision(self.game_objects, self.game_balls)
            for player in self.redteamplayers:
                await player.paddle.checkcolision(self.game_objects, self.game_balls)
            for ballo in self.game_balls:
                scores = await ballo.updateball([self.redscore, self.bluescore])
                if scores[0] != self.redscore or scores[1] != self.bluescore:
                    self.redscore, self.bluescore = scores
                    self.game_balls.remove(ballo)
            if len(self.game_balls) == 0:
                # print('jit hnaya')
                await self.reset_ball()

            # print ('redteamscore: ', self.redscore)
            # print ('blueteamscore: ', self.bluescore)
            # print ('max score is: ', self.max_score)
            # print ('gamestatus: ', self.gamestatus)
            # print ('gamestatus: ', self.gamestatus)

#

            if self.gamestatus == 'ended':
                #do logique to :
                #-->store data in model
                #-->delete room and players can't join it anymore
                print ('handel ended pls')

            # asyncio.drop_bonus()

            # await asyncio.sleep(20)
            
    async def updategame(self, update):
        print(update)
        # print ('gamestatus mn updateball: ', self.gamestatus)

        if not await self.updateGameState(update):
            return
        if self.gamestatus == 'gamestart':
            # print ('lolo : ', self.powerup_task)
            # if self.powerup_task is None:
            #     self.powerup_task = asyncio.create_task(self.spawn_powerup())

            for pl in update:
                if (pl['type'] == 'move'):
                    player = await self.witch_player(pl['player'])
                    if player:
                        # print (player.name)
                        await player.paddle.update(pl['action'])

            
            # current_time = time.time()
            # if current_time - self.lastpowerup >= 5:
            #     print('jit hnaya')
            #     powerup = Powerup()
            #     self.game_objects.append(powerup)
            #     self.lastpowerup = current_time
            
            
            # if len(self.game_balls) == 0:
            #     await self.reset_new_ball()
            #check if score is game over -> reset game
            #check colision with boost
            # self.checkcolision()

    # async def checkcolision_player(self, player):




        #     pass
            #updtae status --> done ?
            #update ball
            #update player
            #update score
        


    def serialize_game_data(self):
        return {
            'redteamplayers' : [player.serialize() for player in self.redteamplayers],
            'blueteamplayers': [player.serialize() for player in self.blueteamplayers],
            'name'           : self.name,
            'status'         : self.gamestatus,
            'gametype'       : self.gametype,
            'winningteam'    : self.winningteam,
            'max_score'      : self.max_score,
            # 'ballside'       : (self.ballside).serialize(),
            # 'redteamball'    : (self.redteamball).serialize(),
            'redfield'       : (self.redfield).serialize(),
            'redscore'       : self.redscore,
            # 'blueteamball'   : (self.blueteamball).serialize(),
            'bluefield'      : (self.bluefield).serialize(),
            'bluescore'      : self.bluescore,
            'powerup'        : [powerup.serialize() for powerup in self.game_objects],
            'balls'          : [ball.serialize() for ball in self.game_balls],
            # 'powerup'        : self.game_objects,
            # 'balls'          : self.game_balls
        }




        async def add_new_bonus(self):
            new_bonus = Bonus(500, 100)
            self.game_objects.append(new_bonus)
