import csv
import json
from Sheep import Sheep
from Wolf import Wolf


class Meadow:
    def __init__(self, number_of_rounds: int, limit_of_sheep: int,
                 limit_of_meadow_x, limit_of_meadow_y):
        self.number_of_rounds = number_of_rounds
        self.limit_of_sheep = limit_of_sheep
        self.limit_of_meadow_x = limit_of_meadow_x
        self.limit_of_meadow_y = limit_of_meadow_y

        self.list_of_sheep = Sheep.create_sheep(limit_of_sheep,
                                                limit_of_meadow_x,
                                                limit_of_meadow_y)
        self.wolf = Wolf("Wolf")

    def move_animals(self):
        Meadow.sheep_alive = len(self.list_of_sheep)

        with open('alive.csv', 'w', newline='') as file, \
                open('pos.json', 'w') as json_file:

            writer = csv.writer(file)
            json_data = []

            for i in range(self.number_of_rounds):
                print("-" * 30 + f"\nRound {i + 1}")
                for sheep in self.list_of_sheep:
                    sheep.move_sheep(self.limit_of_meadow_x,
                                     self.limit_of_meadow_y)
                    # print(sheep.name, sheep.position_x, sheep.position_y)

                ship_alive = self.wolf.move_wolf(self.list_of_sheep)
                round_data = {

                    "round_no": i + 1,
                    "wolf_pos": (self.wolf.position_x, self.wolf.position_y),
                    "sheep_pos": [
                        (sheep.position_x, sheep.position_y)
                        for sheep in self.list_of_sheep
                    ]
                }

                json_data.append(round_data)
                print(f"Number of sheep alive: {ship_alive}")
                # print(self.wolf.name, self.wolf.position_x,
                # self.wolf.position_y)
                writer.writerow([i+1, ship_alive])

                if ship_alive == 0:
                    break
            json.dump(json_data, json_file, indent=3)


meadow = Meadow(50, 15, 10.0, 10.0)
meadow.move_animals()
