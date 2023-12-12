import random


class Sheep:

    def __init__(self, name: str, movement_distance: float, init_pos_limit: float):
        self.name = name
        self.movement_distance = movement_distance
        self.init_pos_limit = init_pos_limit
        self.alive = True
        self.position_x = random.uniform(-init_pos_limit, init_pos_limit)
        self.position_y = random.uniform(-init_pos_limit, init_pos_limit)

    def move_sheep(self):
        direction = random.randint(1, 4)
        if self.alive:
            if direction == 1:
                self.position_x += self.movement_distance
            elif direction == 2:
                self.position_x -= self.movement_distance
            elif direction == 3:
                self.position_y += self.movement_distance
            elif direction == 4:
                self.position_y -= self.movement_distance
            else:
                raise Exception("Invalid direction")

    def is_alive(self):
        return self.alive
