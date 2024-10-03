

#speed  x y R  color 
ball_typo = {
    'default': [20, 30, 10, 10, 'green'],
    'type1'  : [20, 30, 10, 10, 'red'], 
    'type2'  : [20, 30, 10, 10, 'blue'], 
}

class Ball:
    def __init__(self, base, side='red'):
        j = 1 if side == 'red' else -1
        self.speed = ball_typo[base.ball][0]
        self.x = ball_typo[base.ball][1]
        self.y = ball_typo[base.ball][2]
        self.radius = ball_typo[base.ball][3]
        self.color = ball_typo[base.ball][4]

    
    