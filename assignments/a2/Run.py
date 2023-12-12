import argparse
import configparser

from assignments.a2 import Sheep, Wolf, Meadow


def create_sheep(number_of_sheep: int, movement_distance: float,  init_pos_limit: float):
    list_of_sheep = []
    for i in range(number_of_sheep):
        sheep = Sheep.Sheep(f"Sheep {i + 1}", movement_distance, init_pos_limit)
        list_of_sheep.append(sheep)
    return list_of_sheep


parser = argparse.ArgumentParser("Simulation: The Wolf, The Sheep, and The Meadow")
parser.add_argument("-c", "--config", type=str, default="default_config.ini", help="Configuration file")
parser.add_argument("-l", "--log", type=str, help="Log level")
parser.add_argument("-r", "--rounds", type=int, default=50, help="Number of rounds")
parser.add_argument("-s", "--sheep", type=int, default=15, help="Number of sheep")
parser.add_argument("-w", "--wait", action="store_true")

args = parser.parse_args()
if str.split(args.config, ".")[1] != "ini":
    raise Exception("Configuration file must be .ini file")
if args.log:
    if (args.log == "DEBUG"
            or args.log == "INFO"
            or args.log == "WARNING"
            or args.log == "ERROR"
            or args.log == "CRITICAL"):
        print(f"Log level is set to {args.log}")
    else:
        raise Exception("Log level must be DEBUG, INFO, WARNING, ERROR or CRITICAL")
if args.rounds < 1:
    raise Exception("Number of rounds must be greater than 0")
if args.sheep < 1:
    raise Exception("Number of sheep must be greater than 0")
if args.wait:
    print("Program will wait for user input after each round")

config = configparser.ConfigParser()
config.read(args.config)
print(f"Configuration file: {args.config}")

if config.has_option('Sheep', 'InitPosLimit'):
    config_sheep_init_pos_limit = float(config["Sheep"]["InitPosLimit"])
else:
    raise Exception("InitPosLimit is not set in configuration file")
if config.has_option('Sheep', 'MoveDist'):
    config_sheep_movement_distance = float(config["Sheep"]["MoveDist"])
else:
    raise Exception("MoveDist is not set in configuration file")
if config.has_option('Wolf', 'MoveDist'):
    config_wolf_movement_distance = float(config["Wolf"]["MoveDist"])
else:
    raise Exception("MoveDist is not set in configuration file")

sheep_list = create_sheep(args.sheep, config_sheep_movement_distance, config_sheep_init_pos_limit)
wolf = Wolf.Wolf("Wolf", config_wolf_movement_distance)
meadow = Meadow.Meadow(args.rounds, args.sheep, sheep_list, wolf)
meadow.move_animals(args.wait)
