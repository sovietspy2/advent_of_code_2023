from typing import List

FILE_PATH = "/workspaces/advent_of_code_2023/day6/large_input.txt"
DISTANCE = "Distance:"
TIME = "Time:"

def extract_int_array(key: str, line: str):
    line = line[len(key):]
    line = line.strip()
    arr = line.split(" ")
    arr = [int(n) for n in arr if n]
    #print(array_of_time)
    return arr

def load_data():

    tmp_time = None
    tmp_distance = None

    with open(FILE_PATH, "r") as file:
        for line in file:
            
            if (line.startswith(TIME)):
                tmp_time = extract_int_array(DISTANCE, line)

            if (line.startswith(DISTANCE)):
                tmp_distance = extract_int_array(DISTANCE, line)

    return (tmp_time, tmp_distance)

def calculate_winners(time: int, distance: int) -> int:
    solution_count = 0
    for delta_time in range(1, time+1):
        remaining_time = time - delta_time
        move_distance = remaining_time * delta_time
        if (move_distance > distance):
            solution_count = solution_count+1
    return solution_count


time, distance = load_data()

solution = 1

for t,d in zip(time,distance):
    tmp = calculate_winners(t,d)
    solution = solution * tmp

print(solution)

            

