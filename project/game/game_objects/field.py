


#weight color

field_type = {
    'default' : [400, 'grey'],
    'type1' : [400, 'red'],
    'type2' : [400, 'blue'],
}

class Field:
    def __init__(self, base, side='red'):
        # j = 1 if side == 'red' else -1
        self.size = field_type[base.field][0]
        self.color = field_type[base.field][1]
        # print('===>', side)

