# Specify the file path
file_path = '/workspaces/advent_of_code_2023/day1/example.txt'

def extract_first_and_last(input_string):
    first_digit = None
    last_digit = None

    # Finding the first digit (or letter)
    for char in input_string:
        if char.isdigit():
            first_digit = char
            break

    # Finding the last digit (or letter)
    for char in reversed(input_string):
        if char.isdigit():
            last_digit = char
            break

    return first_digit, last_digit

# Open the file in read mode
with open(file_path, 'r') as file:
    sum: int = 0
    # Iterate over each line in the file
    for line in file:
        # Process each line as needed
        #print(line.strip())  # Example: Print each line after removing leading and trailing whitespaces
        first, last = extract_first_and_last(line)
        sum+=int(f"{first}{last}")
        #print(f"for {line} the value is {first}{last}")
    print(f"solution: {sum}")

