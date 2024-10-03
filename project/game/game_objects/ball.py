

#speed  x y R  color 
ball_type = {
    'default': [20, 30, 10, 10, 'green'],
    'type1'  : [20, 30, 10, 10, 'red'], 
    'type2'  : [20, 30, 10, 10, 'blue'], 
}

class Ball:
    def __init__(self, base, side='red'):
        j = 1 if side == 'red' else -1
        self.speed = ball_type[base.ball_type][0]
        self.x = ball_type[base.ball_type][1]
        self.y = ball_type[base.ball_type][2]
        self.radius = ball_type[base.ball_type][3]
        self.color = ball_type[base.ball_type][4]

    
    