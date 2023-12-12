import random

from assignments.a2.logger import Logger


class Sheep:
    direction = {
        1: "WEST",
        2: "EAST",
        3: "NORTH",
        4: "SOUTH"
    }

    def __init__(self, name: str, movement_distance: float,
                 init_pos_limit: float,
                 logger: Logger = None):
        self.name = name
        self.movement_distance = movement_distance
        self.init_pos_limit = init_pos_limit
        self.alive = True
        self.position_x = random.uniform(-init_pos_limit, init_pos_limit)
        self.position_y = random.uniform(-init_pos_limit, init_pos_limit)
        self.logger = logger

    def move_sheep(self):
        if self.alive:
            direction = random.randint(1, 4)
            if self.logger:
                self.logger.log("DEBUG", f"{self.name} chose {self.direction[direction]}")
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

                if self.logger:
                    self.logger.log("DEBUG", f"{self.name} moved to {self.position_x}, {self.position_y}")

    def is_alive(self):
        return self.alive
