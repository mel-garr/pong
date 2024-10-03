# anbedel had base.width/heigh mnin ndeber fchi db bach automotiauement tqkhdhoum mn tem
# wid spells 


#width, height , color, x, y
paddle_type = {
    'default':[10, 30, 'green', 20 , 300],
    'type1':[10, 30, 'red', 20 , 300],
    'type2':[10, 30, 'blue', 20 , 300],
}

class Paddle:
    def __init__(self, base, side, i):
        self.width = paddle_type[base.paddle_type][0]
        self.hight = paddle_type[base.paddle_type][1]
        self.color = paddle_type[base.paddle_type][2]
        self.x = paddle_type[base.paddle_type][3]
        self.y = paddle_type[base.paddle_type][4]
