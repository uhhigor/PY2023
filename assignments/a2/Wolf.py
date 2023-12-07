import math


class Wolf:
    def __init__(self, name: str, initial_position_x=0.0,
                 initial_position_y=0.0, movement_distance=1.0):
        self.name = name
        self.position_x = initial_position_x
        self.position_y = initial_position_y
        self.movement_distance = movement_distance

    def move_wolf(self, list_of_sheep: list):
        closest_sheep_distance = float('inf')
        closest_sheep = None
        for sheep in list_of_sheep:
            sheep_distance = math.sqrt((self.position_x - sheep.position_x) ** 2 + (self.position_y - sheep.position_y) ** 2)
            if sheep_distance <= self.movement_distance:
                list_of_sheep.remove(sheep)
                print(f"Wolf ate a {sheep.name}")
                self.position_x = sheep.position_x
                self.position_y = sheep.position_y
                return
            elif sheep_distance < closest_sheep_distance:
                closest_sheep_distance = sheep_distance
                closest_sheep = sheep
        self.position_x += (closest_sheep.position_x - self.position_x) / closest_sheep_distance * self.movement_distance
        self.position_y += (closest_sheep.position_y - self.position_y) / closest_sheep_distance * self.movement_distance
        print(f"Wolf moved to {self.position_x}, {self.position_y}")
