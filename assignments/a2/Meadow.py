from Sheep import Sheep
from Wolf import Wolf


class Meadow:

    def __init__(self, limit_of_meadow: float, limit_of_sheep: int, number_of_rounds: int):
        self.limit_of_meadow = limit_of_meadow
        self.limit_of_sheep = limit_of_sheep
        self.number_of_rounds = number_of_rounds
        self.list_of_sheep = Sheep.create_sheep(limit_of_sheep, limit_of_meadow)
        self.wolf = Wolf("Wolf")

    def move_animals(self):
        for i in range(self.number_of_rounds):
            print(f"Round {i + 1}")
            for sheep in self.list_of_sheep:
                sheep.move_sheep(self.limit_of_meadow)
                print(sheep.name, sheep.position_x, sheep.position_y, sheep.movement_distance)
            self.wolf.move_wolf(self.list_of_sheep)
            print(self.wolf.name, self.wolf.position_x, self.wolf.position_y, self.wolf.movement_distance)


meadow = Meadow(10.0, 15, 5)
meadow.move_animals()
