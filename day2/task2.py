from dataclasses import dataclass, field
import re

#defined in task
available_red = 12
available_green = 13
available_blue = 14

red_pattern = re.compile(r'(\d+) red')
blue_pattern = re.compile(r'(\d+) blue')
green_pattern = re.compile(r'(\d+) green')
game_pattern = re.compile(r'Game (\d+):')


file_path: str = "/workspaces/advent_of_code_2023/day2/input.txt"
lines: list[str] = []

#loading example data
with open (file_path, 'r') as file:
    for line in file:
        lines.append(line)

@dataclass
class GameSet:
    red: int
    green: int
    blue: int

    def is_possible(self):
            return self.red <= available_red and self.green <= available_green and self.blue <= available_blue

@dataclass
class Game:
    game_id: int
    game_sets: list[GameSet] = field(default_factory=list)

    def is_possible(self):
        #print(f"sum r: {sum_red} g {sum_green} b {sum_blue}")
        return all(game_set.is_possible() for game_set in self.game_sets)


def transform_data_to_objects(lines):
    games = []
    for current_line in lines:
        array_of_game_sets = current_line.split(";")
        game_id = extract_game_id(array_of_game_sets[0])
        game = Game(game_id=game_id)
        games.append(game)
        for game_set in array_of_game_sets:
            red, green, blue = extract_colors(game_set)
            #print(game_set)
            game_set_instance = GameSet(red, green, blue)
            game.game_sets.append(game_set_instance)
    return games

def extract_game_id(first_game_set):
    matches = game_pattern.findall(first_game_set)
    #print(matches)
    for match in matches:
        print(f"Extracted game id is: {match}")
        return int(match)
    

def extract_colors(game_set):
    red, green, blue = 0,0,0

    matches = red_pattern.findall(game_set)

    for match in matches:
        red = int(match);

    matches = green_pattern.findall(game_set)

    for match in matches:
        green = int(match);

    matches = blue_pattern.findall(game_set)

    for match in matches:
        blue = int(match);

    #print(f"red: {red} green: {green} blue: {blue}")
    return red, green, blue
    

games = transform_data_to_objects(lines)

solution = sum(game.game_id for game in games if game.is_possible())

print(solution)