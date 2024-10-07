

#speed  x y R  color 
ball_typo = {
    'default': [300, 400, 300, 10, 'green'],
    'type1'  : [300, 400, 300, 15, 'red'], 
    'type2'  : [300, 400, 300, 20, 'blue'], 
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

    def serialize(self):
        return {
            'speed' : self.speed,
            'x'     : self.x,
            'y'     : self.y,
            'radius': self.radius,
            'color' : self.color,
        }
    
    