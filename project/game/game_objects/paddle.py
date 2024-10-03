# anbedel had base.width/heigh mnin ndeber fchi db bach automotiauement tqkhdhoum mn tem
# wid spells 


#width, height , color, x, y
paddle_type = {
    'default':[10, 30, 'green', 20 , 300],
    'type1'  :[10, 30, 'red'  , 20 , 300],
    'type2'  :[10, 30, 'blue' , 20 , 300],
}

paddle_spacing = 10

class Paddle:
    def __init__(self, base, side, i):
        j = 1 if side == 'red' else -1
        self.width = paddle_type[base.paddle][0]
        self.hight = paddle_type[base.paddle][1]
        self.color = paddle_type[base.paddle][2]
        self.x = (paddle_type[base.paddle][3] + (i * paddle_spacing)) * j
        self.y = paddle_type[base.paddle][4]

    
