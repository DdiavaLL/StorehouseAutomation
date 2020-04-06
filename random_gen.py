import random

class RandomGen:
    def __init__(self, x_length, y_length):
        self.x = x_length
        self.y = y_length

    def rand_box_gen(self, count):
        rez = []
        for i in range(0, count):
            new_x = random.randint(0, self.x)
            rez.append([new_x, new_x])
        return rez
