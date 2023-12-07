import random


class Sheep:
    def __init__(self, name: str, initial_position_x: float, initial_position_y: float, movement_distance=0.5):
        self.name = name
        self.position_x = initial_position_x
        self.position_y = initial_position_y
        self.movement_distance = movement_distance

    @staticmethod
    def create_sheep(number_of_sheep: int, limit_of_meadow: float):
        list_of_sheep = []
        for i in range(number_of_sheep):
            position_x = random.uniform(-limit_of_meadow, limit_of_meadow)
            position_y = random.uniform(-limit_of_meadow, limit_of_meadow)
            sheep = Sheep(f"Sheep {i+1}", position_x, position_y)
            list_of_sheep.append(sheep)
        return list_of_sheep

    def move_sheep(self, limit_of_meadow: float):
        direction = random.randint(1, 4)
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

        if self.position_x > limit_of_meadow:
            self.position_x = limit_of_meadow
        elif self.position_x < -limit_of_meadow:
            self.position_x = -limit_of_meadow
        if self.position_y > limit_of_meadow:
            self.position_y = limit_of_meadow
        elif self.position_y < -limit_of_meadow:
            self.position_y = -limit_of_meadow
        return self.position_x, self.position_y
