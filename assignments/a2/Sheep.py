import random


class Sheep:
    def __init__(self, name: str, position_x: float,
                 position_y: float, movement_distance=0.5):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.movement_distance = movement_distance
        self.alive = True

    @staticmethod
    def create_sheep(number_of_sheep: int, limit_of_meadow_x: float,
                     limit_of_meadow_y: float):
        list_of_sheep = []
        for i in range(number_of_sheep):
            position_x = random.uniform(-limit_of_meadow_x, limit_of_meadow_x)
            position_y = random.uniform(-limit_of_meadow_y, limit_of_meadow_y)
            sheep = Sheep(f"Sheep {i+1}", position_x, position_y)
            list_of_sheep.append(sheep)
        return list_of_sheep

    def move_sheep(self, limit_of_meadow_x: float, limit_of_meadow_y: float):
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
                print("Error")

            if self.position_x > limit_of_meadow_x:
                self.position_x = limit_of_meadow_x
            elif self.position_x < -limit_of_meadow_x:
                self.position_x = -limit_of_meadow_x
            if self.position_y > limit_of_meadow_y:
                self.position_y = limit_of_meadow_y
            elif self.position_y < -limit_of_meadow_y:
                self.position_y = -limit_of_meadow_y

    def is_alive(self):
        return self.alive
