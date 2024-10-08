
# anbedel had base.width/heigh mnin ndeber fchi db bach automotiauement tqkhdhoum mn tem
# wid spells 


#width, height , color, x, y
paddle_type = {
    'default':[10, 100, 'green', 20 , 300, 5],
    'type1'  :[10, 30, 'red'  , 20 , 300, 5],
    'type2'  :[10, 30, 'blue' , 20 , 300, 5],
}

paddle_spacing = 10

class Paddle:
    def __init__(self, base, side, i, name):
        j = 0 if side == 'red' else 800
        self.name = name
        self.width = paddle_type[base.paddle][0]
        self.height = paddle_type[base.paddle][1]
        self.color = paddle_type[base.paddle][2]
        self.x = j - (paddle_type[base.paddle][3] + (i * paddle_spacing)) if side == 'blue' else (paddle_type[base.paddle][3] + (i * paddle_spacing))
        self.y = paddle_type[base.paddle][4] - self.height / 2
        self.dy = paddle_type[base.paddle][5]

    def serialize(self):
        return {
            'width' : self.width,
            'height': self.height,
            'color' : self.color,
            'x'     : self.x,
            'y'     : self.y,
        }
    
    async def update(self, move):
        if (move == 'up'):
            self.y = max(0, self.y - self.dy)
        
        if (move == 'down'):
            self.y = min(600 - self.height , self.y + self.dy)

    async def checkcolision_s(self, obj):

        return (
            obj.x + obj.radius > self.x and
            obj.x - obj.radius < self.x + self.width and  
            obj.y + obj.radius > self.y and 
            obj.y - obj.radius < self.y + self.height
        )


    async def checkcolision(self, bonus, objects):
        for obj in objects:
            if (await self.checkcolision_s(obj)):
                await obj.ball_interaction(self)

        # for obj in bonus:
        #     if (await checkcolision_s(obj)):
        #         await obj.bonus_interaction()
                
    
