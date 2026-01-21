# Day 15: Science for Hungry People

from itertools import product

# Ingredient class
class Ingredient:
    def __init__(self, name, cap, dur, fla, tex, cal):
        self.name = name
        self.capacity = cap
        self.durability = dur
        self.flavor = fla
        self.texture = tex
        self.calories = cal


# Parts 1 and 2 (determined by the calorie_count variable)
def maximizeScore(ingrs: list[Ingredient], tsps: int, calorie_count: int = 0):
    # Generate all possible combinations of 4 digits that add to 100
    all_combos = [i for i in product(range(tsps + 1), repeat=len(ingrs)) if sum(i) == tsps]
    max_score = 0
    total_cap, total_dur, total_fla, total_tex, total_cal = 0, 0, 0, 0, 0

    # Loop through all possible combos
    for combo in all_combos:
        for i in range(len(ingrs)):
            total_cap += combo[i] * ingrs[i].capacity
            total_dur += combo[i] * ingrs[i].durability
            total_fla += combo[i] * ingrs[i].flavor
            total_tex += combo[i] * ingrs[i].texture
            total_cal += combo[i] * ingrs[i].calories
        
        # If our total calories is not equal to the specified calorie count (if defined, otherwise ignore if 0) or if any variable is less than 0 this result should be ignored
        if (calorie_count == 0 or total_cal == calorie_count) and total_cap > 0 and total_dur > 0 and total_fla > 0 and total_tex > 0:
            max_score = max(total_cap * total_dur * total_fla * total_tex, max_score)
        
        total_cap, total_dur, total_fla, total_tex, total_cal = 0, 0, 0, 0, 0

    return max_score


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day15.txt", "r") as f:
            line = f.readline()
            ingrs = []
            while line:
                # Split the line by spaces and trim the last character of each item if it is not alphanumeric (i.e. ":" or ",")
                split_line = [i[:-1] if not i[-1].isalnum() else i for i in line.split()]
                # Further prune the list by including only the even-indexed terms
                split_line = [split_line[i] for i in range(len(split_line)) if i % 2 == 0]
                # Assign each item to its respective variable, converting them to integers if needed
                name, capacity, durability, flavor, texture, calories = [int(split_line[i]) if i != 0 else split_line[i] for i in range(len(split_line))]
                ingrs.append(Ingredient(name, capacity, durability, flavor, texture, calories))
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"The highest-scoring cookie that can be made outright has a score of {maximizeScore(ingrs, 100)}.")  # Part 1

    calorie_count = 500
    print(f"The highest-scoring cookie that can be made with a calorie total of exactly {calorie_count} has a score of {maximizeScore(ingrs, 100, calorie_count)}.")  # Part 2