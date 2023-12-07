
import re
FILE_PATH = "/workspaces/advent_of_code_2023/day7/small_input.txt"


def extract(line):
    pattern = r'(\S+)\s+(\d+)'  # Matches two groups of digits separated by one or more spaces
    match = re.match(pattern, line)
    
    if match:
        # Extracting the two integer values
        hand = str(match.group(1))
        score = int(match.group(2))
        return hand, score
    
def custom_string_comparison(item):
    return len(item[1])

# Sorting the list using the custom comparison
#sorted_list = sorted(my_list, key=custom_string_comparison, reverse=True)


list_of_data = list()

with open(FILE_PATH, "r") as file:
    for line in file:
        list_of_data.append(extract(line))


for i in list_of_data:
    print(i)


