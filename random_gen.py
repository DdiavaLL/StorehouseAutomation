import random

class RandomGen:
    def __init__(self, x_length, y_length):
        self.x = x_length
        self.y = y_length

    def rand_box_gen(self, count):
        rez = []
        for i in range(0, count):
            new_x = random.randrange(1, self.x, 1)
            new_y = random.randrange(1, self.y, 1)
            rez.append([new_x, new_y])
        return rez
