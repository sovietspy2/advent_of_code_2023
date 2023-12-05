FILE_PATH = '/workspaces/advent_of_code_2023/day3/large_input.txt'
SYMBOLS = ["#", "*", "$", "+", "/", "@", "=", "%", "&", "^", "-", "\\" ]

class PartNumber:
    def __init__(self) -> None:
        self.coordinates = list()
        self.actual_values = list()
    def __str__(self) -> str:
        return f'PartNumber coordinates: {self.coordinates} actual value: {"".join(self.actual_values)}'

    def get_number(self) -> int:
        return int("".join(self.actual_values))

matrix = list()

with open(FILE_PATH, "r") as file:
    for line in file:
        matrix.append(list(line.strip()))

def find_all_PartNumbers(matrix):
    part_numbers = list()
    for row_index, line in enumerate(matrix,0):
        part_number = None
        for column_index, row_item in enumerate(line,0):
            if (row_item in SYMBOLS or row_item == "."):
                #print("it's a SYMBOL!")
                part_number = None
            else:
                if (part_number is None):
                    part_number = PartNumber()
                    part_numbers.append(part_number)
                part_number.actual_values.append(matrix[row_index][column_index])
                part_number.coordinates.append((row_index, column_index))
    return part_numbers

def find_adjecent_indexes_for_PartNumber(matrix, part_number: PartNumber):
    ROW_MAX = len(matrix)
    COLUMN_MAX = len(matrix[0])
    indexes = list()

    for coordinate in part_number.coordinates:
        row_index, column_index = coordinate

        adjacent_coordinates = [
            (row_index - 1, column_index),
            (row_index - 1, column_index +1),
            (row_index - 1, column_index -1),
            (row_index + 1, column_index),
            (row_index + 1, column_index+1),
            (row_index + 1, column_index-1),
            (row_index, column_index +1),
            (row_index, column_index -1)
        ]

        indexes = indexes + adjacent_coordinates
    return indexes




def check_coordinates_for_symbols(matrix, coordinates: list):
    found_symbol = False
    for coordinate in coordinates:
        x,y = coordinate
        try:
            if matrix[x][y] in SYMBOLS:
                found_symbol = True
        except IndexError:
            pass
    return found_symbol

    

def find_solution(matrix, part_numbers: list[PartNumber]):

    solution_sum = 0

    for part_number in part_numbers:
        adjecent_cooridantes = find_adjecent_indexes_for_PartNumber(matrix, part_number)
        if (check_coordinates_for_symbols(matrix, adjecent_cooridantes)):
            print(f"we found a solution: {part_number}")
            solution_sum = solution_sum + part_number.get_number()

    print(solution_sum)
    


part_numbers = find_all_PartNumbers(matrix)

find_solution(matrix, part_numbers)

