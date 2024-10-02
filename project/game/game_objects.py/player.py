class PLayer:
    def __init__(self, name, position, paddle):
        self.name = name
        # data token from the object position
        self.x = position.x
        self.y = position.y
        # data token fro; the class paddle
        self.width = paddle.width
        self.height = paddle.height
        self.speed = paddle.speed
        self.color = paddle.color

        
        