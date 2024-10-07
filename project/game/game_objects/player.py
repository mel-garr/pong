from .paddle import Paddle
from .ball import Ball
from .field import Field
 

class Player:
    def __init__(self, base, i, side='red'):
        self.name = base.name
        # self.side = side
        # data token from the object position
        self.paddle = Paddle(base, side, i)
        self.ball = Ball(base, side)
        self.field = Field(base, side)

        
        # data token fro; the class paddle

    def serialize(self):
        return {
            'name'   : self.name,
            'paddle' : self.paddle.serialize(),
            # 'ball'   : self.ball.serialize(),
            'field'  : self.field.serialize(),
        }


        