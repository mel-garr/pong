

#speed  x y R  color 
ball_typo = {
    'default': [300, 400, 300, 10, 'green', 5],
    'type1'  : [300, 400, 300, 15, 'red', 5], 
    'type2'  : [300, 400, 300, 20, 'blue', 5], 
}

class Ball:
    def __init__(self, base, side='red'):
        j = 1 if side == 'red' else -1
        self.speed = ball_typo[base.ball][0]
        self.x = ball_typo[base.ball][1]
        self.y = ball_typo[base.ball][2]
        self.radius = ball_typo[base.ball][3]
        self.color = ball_typo[base.ball][4]
        self.side = side
        self.dx = ball_typo[base.ball][5] 
        self.dy = ball_typo[base.ball][5] 
        self.lasttouch = None

    def serialize(self):
        return {
            'speed' : self.speed,
            'x'     : self.x,
            'y'     : self.y,
            'radius': self.radius,
            'color' : self.color,
        }
    
    async def updateball(self, PS1, PS2):
    
        if (self.y + self.radius) >= 600 or (self.y - self.radius) <= 0:
            self.dy *= -1
        
        if (self.x >= 800 - self.radius) or (self.x - self.radius) <= 0:
            self.dx *= -1
            # return (0)
        # return 1
            #need to update the game and score if x

        self.x += self.dx
        self.y += self.dy

    async def ball_interaction(self, paddle):
        self.lasttouch = paddle.name
        self.dx *= -1

    async def ball_colision_bonus(self, objects):
        pass
    

    