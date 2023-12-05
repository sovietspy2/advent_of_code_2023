FILE_INPUT = "/workspaces/advent_of_code_2023/day4/large_input.txt"
import re
from collections import Counter
import math

card_number_pattern = r"Card (\d+):"

def extract_card_number(line: str):
    match = re.search(card_number_pattern, line)
    if match:
        return match.group(1)
    
def score_to_sum(match_count: int):

    if (match_count==0):
        return 0

    v = 1
    for _ in range(match_count-1):
        v = v * 2
    return v

scores = list()

with open(FILE_INPUT, "r") as file:
    for line in file:
        
        #extract card number
        card_number = extract_card_number(line)

        #remove first part of the string: "Card X:"
        line = line[7:]

        #clean the string start and end
        line = line.strip()

        numbers = line.split("|")
        winning_numbers = numbers[0].split(" ")
        playing_numbers = numbers[1].split(" ")

        #clean from spaces
        winning_numbers = [number for number in winning_numbers if number.isdigit()]
        playing_numbers = [number for number in playing_numbers if number.isdigit()]

        print("=======")
        print(f"winning numbers:  {winning_numbers}")
        print(f"playing numbers: {playing_numbers}")

        winning_counter = Counter(winning_numbers)
        playing_counter = Counter(playing_numbers)

        # Get the intersection of the counters
        intersection_counter = winning_counter & playing_counter

        # Sum the counts of overlapping elements
        overlapping_count = sum(intersection_counter.values())

        print(f" {card_number} card: score {score_to_sum(overlapping_count)} intersection: {intersection_counter.keys()}")
        scores.append(score_to_sum(overlapping_count))

sum = sum(scores)

print(sum)