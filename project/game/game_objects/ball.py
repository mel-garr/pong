

#speed  x y R  color 
ball_typo = {
    'default': [300, 400, 300, 10, 'green', 5],
    'type1'  : [300, 400, 300, 15, 'red', 5], 
    'type2'  : [300, 400, 300, 20, 'blue', 5], 
}

class Ball:
    def __init__(self, base, side='red'):
        j = 1 if side == 'red' else -1
        self.ball_type = base
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
    
    async def clone(self):
        new_ball = Ball(self.ball_type, self.side)
        new_ball.speed = self.speed
        new_ball.x = self.x
        new_ball.y = self.y
        new_ball.radius = self.radius
        new_ball.color = self.color
        new_ball.dx = self.dx
        new_ball.dy = self.dy
        new_ball.lasttouch = self.lasttouch
        new_ball.side = self.side
        return new_ball

    async def updateball(self, scores):
    
        # scores[0] = 15
        if (self.y + self.radius) >= 600 or (self.y - self.radius) <= 0:
            self.dy *= -1
        
        if (self.x >= 800 - self.radius):
            scores[0] += 1
            # self.dx *= -1
        
        if (self.x - self.radius) <= 0:
            scores[1] += 1
            # self.dx *= -1
        # print ('9abel: ', scores[0])
            
        # print ('yoo')
        self.x += self.dx
        self.y += self.dy
        # print ('beeeee3: ',scores[0])
        return scores

    async def ball_interaction(self, paddle):
        self.lasttouch = paddle.name
        self.dx *= -1

    async def ball_colision_bonus(self, objects):
        pass
    

    