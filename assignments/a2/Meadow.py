import csv
import json

from Sheep import Sheep
from Wolf import Wolf
from assignments.a2.logger import Logger


class Meadow:
    def __init__(self, number_of_rounds: int, limit_of_sheep: int,
                 list_of_sheep: list[Sheep], wolf: Wolf,
                 logger: Logger = None):
        self.number_of_rounds = number_of_rounds
        self.limit_of_sheep = limit_of_sheep
        self.list_of_sheep = list_of_sheep
        self.wolf = wolf
        self.logger = logger

    def move_animals(self, wait=False):
        Meadow.sheep_alive = len(self.list_of_sheep)

        with open('alive.csv', 'w', newline='') as file, \
                open('pos.json', 'w') as json_file:

            writer = csv.writer(file)
            json_data = []

            for i in range(self.number_of_rounds):
                if self.logger:
                    self.logger.log("INFO", f"Round {i + 1} started.")
                print("-" * 30 + f"\nRound {i + 1}")
                for sheep in self.list_of_sheep:
                    sheep.move_sheep()

                if self.logger:
                    self.logger.log("INFO", "All alive sheep moved.")

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
                writer.writerow([i + 1, ship_alive])
                if self.logger:
                    self.logger.log("DEBUG", "Information saved to: alive.csv")

                if ship_alive == 0:
                    if self.logger:
                        cause = "All sheep have been eaten."
                    break

                if self.logger:
                    self.logger.log("INFO", f"Round {i + 1} ended. Number of sheep alive: {ship_alive}")

                if wait:
                    input("Press Enter to continue...")

                if self.logger:
                    cause = "Maximum number of rounds has been reached."

            json.dump(json_data, json_file, indent=3)
            if self.logger:
                self.logger.log("DEBUG", "Information saved to: pos.json")
                self.logger.log("INFO", f"Simulation ended. {cause}")
