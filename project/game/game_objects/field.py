


#weight color

field_type = {
    'default' : [400, 'orange', 600],
    'type1' : [400, 'black', 600],
    'type2' : [400, 'blue', 600],
}

class Field:
    def __init__(self, base, side='red'):
        # j = 1 if side == 'red' else -1
        self.width = field_type[base.field][0]
        self.color = field_type[base.field][1]
        self.height = field_type[base.field][2]

        # print('===>', side)

