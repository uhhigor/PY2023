import math


class Wolf:

    def __init__(self, name: str, initial_position_x=0.0,
                 initial_position_y=0.0, movement_distance=1.0):
        self.name = name
        self.position_x = initial_position_x
        self.position_y = initial_position_y
        self.movement_distance = movement_distance

    def move_wolf(self, list_of_sheep: list):
        if sum(1 for sheep in list_of_sheep if sheep.is_alive()) == 0:
            return 0

        closest_sheep_distance = float('inf')
        closest_sheep = None

        for i, sheep in enumerate(list_of_sheep):

            if not sheep.is_alive():
                continue

            sheep_distance = math.sqrt((self.position_x
                                        - sheep.position_x) ** 2
                                       + (self.position_y
                                          - sheep.position_y) ** 2)

            if sheep_distance <= self.movement_distance \
                    or len(list_of_sheep) == 1:
                self.position_x = sheep.position_x
                self.position_y = sheep.position_y
                print(f"Wolf moved to {round(self.position_x, 3)}, "
                      f"{round(self.position_y, 3)}"
                      + f"\nWolf ate a {sheep.name}")
                sheep.position_x = None
                sheep.position_y = None
                sheep.alive = False
                # list_of_sheep.remove(sheep)
                list_of_sheep[i] = sheep
                return sum(1 for sheep in list_of_sheep if sheep.is_alive())

            elif sheep_distance < closest_sheep_distance:
                closest_sheep_distance = sheep_distance
                closest_sheep = sheep

        self.position_x += ((closest_sheep.position_x - self.position_x) /
                            closest_sheep_distance * self.movement_distance)
        self.position_y += ((closest_sheep.position_y - self.position_y) /
                            closest_sheep_distance * self.movement_distance)
        print(f"Wolf moved to {round(self.position_x, 3)}, "
              f"{round(self.position_y, 3)}"
              + f"\nWolf is chasing a {closest_sheep.name}")

        return sum(1 for sheep in list_of_sheep if sheep.is_alive())
