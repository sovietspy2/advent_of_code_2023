FILE_LOCATION = "/workspaces/advent_of_code_2023/day5/large_input.txt"
from typing import List

class Range:
    def __init__(self, destination_start: int, source_start: int, size: int) -> None:
        self.source_start = source_start
        self.destination_start = destination_start
        self.lag = self.destination_start - self.source_start
        self.size = size

    def get_end(self, start: int):
        return start + (self.size-1)

    def include_code(self, code: int):
        return (code >= self.source_start and code <= self.get_end(self.source_start)) 

    def translate_code(self, code: int):
        if self.include_code(code):
            return code + self.lag
        
        

class GardenMap:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ranges: List[Range] = list()

    def add_range(self, source_start: int, destination_start: int, size: int):
        self.ranges.append(Range(source_start, destination_start, size))

    def translate(self, code: int):

        found_value = None

        for range in self.ranges:
            if range.include_code(code):
                found_value = range.translate_code(code)

        
        r = code if found_value is None else found_value
        print(f"{self.name} {code}->{r}")

        return r
        
    def __str__(self) -> str:
        return f"name: {self.name} ranges: {self.ranges}"



def load_data():

    seeds = None
    maps: List[GardenMap] = list()

    control = ["seeds:", "seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:",
              "water-to-light map:",  "light-to-temperature map:", "temperature-to-humidity map:",
              "humidity-to-location map:"]
    
    current_control_item = control.pop(0)
    current_map: GardenMap = None

    with open(FILE_LOCATION, "r") as file:
        for line in file:

            line = line.strip()
            #print(line)

            #unique case
            if (current_control_item == "seeds:" and seeds is None):
                #clean empty values

                 #remove control world if its present
                if (line.startswith(current_control_item)):
                    line = line[len(current_control_item):]

                #clean the line
                array_of_numbers = line.split(" ")

                 #cast to int
                array_of_numbers = [int(number) for number in array_of_numbers if number]
                
                print(f"Seeds: ", array_of_numbers)

                seeds = array_of_numbers
            
            #check if line not blank
            elif  bool(line.strip()):

                # If we see another control key than we opened a new map
                control_change = any(control_key in line for control_key in control)

                if control_change:
                    current_control_item = control.pop(0)
                    current_map = GardenMap(current_control_item)
                    maps.append(current_map)
                else:
                    #clean the line
                    array_of_numbers = line.split(" ")
                    array_of_numbers = [int(number) for number in array_of_numbers if number]

                    current_map.add_range(array_of_numbers[0], array_of_numbers[1], array_of_numbers[2])

    return (seeds, maps)

def find_soluiton(seeds: List[int], maps: List[GardenMap]):
    lowest = None

    for seed in seeds:

        temp_code = seed
        for map in maps:
            temp_code = map.translate(temp_code)
        
        #after last map iteration the temp_code is the location
        if (lowest is None or temp_code < lowest):
            lowest = temp_code

        print(f"for {seed} we got {temp_code}")

    return lowest

seeds, maps = load_data()

print(find_soluiton(seeds, maps))