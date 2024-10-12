
    #power up for paddle
        #shape bigger shorter
        #speed fast slow 
        #magic freez changedirection
    #ball
        #shape small big
        #speed fasr slow stop in time
        #magic duplicateball , double score , break paddle
    #field
        #shape take more space 
        #slowplayer and ball
        #magic invsibility freez_everything_except_the_player

import random

powerup_type = {
    'a' : ['paddleB','red', 5],   #bigger paddle
    'b' : ['paddles', 'blue', 5], #shorter player
} 

class Powerup:
    def __init__(self):
        powerup = random.choice(list(powerup_type.items()))
        # print ('jit foust powerup-----------------------')
        self.name = powerup[0]
        self.color = powerup[1][1]
        self.radius = powerup[1][2]
    # self.name = powerup_type[0]
        self.x = random.randint(self.radius, 800 - self.radius)
        self.y = random.randint(self.radius, 600 - self.radius)
        

    def serialize(self):
        return {
            'speed' : self.name,
            'x'     : self.x,
            'y'     : self.y,
            'radius': self.radius,
            'color' : self.color,
        }

    async def spawn_powerup():
        powerup = Powerup()
        print(f"Bonus spawned: {bonus.name} at ({bonus.x}, {bonus.y})")

        await asyncio.sleep(5)
        return powerup
