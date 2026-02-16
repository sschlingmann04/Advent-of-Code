# Day 11: Radioisotope Thermoelectric Generators

from collections import deque
from itertools import combinations


def isValid(state):
    _, pairs = state

    floors = {1: {"chips": set(), "gens": set()},
              2: {"chips": set(), "gens": set()},
              3: {"chips": set(), "gens": set()},
              4: {"chips": set(), "gens": set()}}

    for i, (chip, gen) in enumerate(pairs):
        floors[chip]["chips"].add(i)
        floors[gen]["gens"].add(i)

    for f in floors.values():
        if f["gens"]:  # at least one generator
            for chip_id in f["chips"]:
                if chip_id not in f["gens"]:
                    return False

    return True

def generateMoves(state):
    floor, pairs = state
    items = []
    for i, (chip, gen) in enumerate(pairs):
        if chip == floor:
            items.append((0, i))
        if gen == floor:
            items.append((1, i))

    if not items:
        return []

    next_states = []
    for r in (1, 2):  # can move 1 or 2 items
        for combo in combinations(items, r):
            # UP
            if floor < 4:
                new_pairs = [list(p) for p in pairs]
                for item_type, index in combo:
                    new_pairs[index][item_type] = floor + 1
                new_pairs_tuple = tuple(sorted(tuple(p) for p in new_pairs))
                next_states.append((floor + 1, new_pairs_tuple))

            # DOWN: only if there are items below
            if floor > 1:
                has_below = any(c < floor or g < floor for c, g in pairs)
                if has_below:
                    new_pairs = [list(p) for p in pairs]
                    for item_type, index in combo:
                        new_pairs[index][item_type] = floor - 1
                    new_pairs_tuple = tuple(sorted(tuple(p) for p in new_pairs))
                    next_states.append((floor - 1, new_pairs_tuple))

    return next_states


def hasItemsBelow(floor, pairs):
    for chip, gen in pairs:
        if chip < floor or gen < floor:
            return True
    return False

def goalReached(state):
    floor, pairs = state
    if floor != 4:
        return False
    return all(c == 4 and g == 4 for c, g in pairs)



# Part 1
def calculateMinimumSteps(elevator: tuple[int, tuple[tuple[int, int]]]):
    queue = deque([(elevator, 0)])
    seen = set([elevator])

    while queue:
        state, steps = queue.popleft()

        if goalReached(state):
            return steps
        
        for new_state in generateMoves(state):
            if isValid(new_state) and new_state not in seen:
                seen.add(new_state)
                queue.append((new_state, steps + 1))


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day11.txt", "r") as f:
            line = f.readline().strip()
            elements = {}
            chips, generators = [], []
            current_floor = 1

            while line:
                contents = line.split(" contains ")[1].strip(".")
                split_line = contents.split()
                for index, word in enumerate(split_line):
                    if word == "generator":
                        element = split_line[index - 1]
                        if element not in elements:
                            elements[element] = len(elements)
                            chips.append(0)
                            generators.append(0)
                        generators[elements[element]] = current_floor
                    elif word == "microchip":
                        element = split_line[index - 1].split("-")[0]
                        if element not in elements:
                            elements[element] = len(elements)
                            chips.append(0)
                            generators.append(0)
                        chips[elements[element]] = current_floor
                
                current_floor += 1
                line = f.readline().strip()
            
            pairs = tuple(sorted((chips[i], generators[i]) for i in range(len(chips))))
            elevator = (1, pairs)
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"To bring all of the objects to the fourth floor, it will take at least {calculateMinimumSteps(elevator)} steps.")  # Part 1