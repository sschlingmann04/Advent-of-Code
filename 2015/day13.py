# Day 13: Knights of the Dinner Table

from itertools import permutations

# Parts 1 and 2 (setup for part 2 is in the main program)
def findOptimalSeating(table: dict):
    # Get all possible permutations of seating arrangements
    arrangements = list(permutations(names))
    max_happiness = 0
    current_happiness = 0

    # Loop through each possible arrangement
    for arrangement in arrangements:
        # Loop through each name in the seating arrangement
        for name in range(len(arrangement)):
            next_name = arrangement[name + 1] if name != len(arrangement) - 1 else arrangement[0]  # Seating arrangement is circular so it should return back to the first name
            name = arrangement[name]
            # Loop through each combination of seating pairs in the happiness table
            for pair in table:
                # If both names are in the pair the add the happiness score to the current_happiness variable
                if name in pair and next_name in pair:
                    current_happiness += table[pair]
                    break  # Break out and move on to the next pair of names
        
        # Update max_happiness if a new maximum is found
        max_happiness = max(max_happiness, current_happiness)
        current_happiness = 0
    
    return max_happiness


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day13.txt", "r") as f:
            line = f.readline()
            table = {}
            names = set()
            while line:
                pt1, pt2 = line.split(" happiness units by sitting next to ")
                person2 = pt2.strip(".\n")
                person1, happiness = pt1.split(" would ")

                happiness = int(happiness[5:]) if happiness.startswith("gain") else -int(happiness[5:])

                persons = tuple(sorted([person1, person2]))
                if table.get(persons) is None:
                    table[persons] = happiness
                else:
                    table[persons] += happiness
                
                names.add(person1)
                names.add(person2)
                
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")

    print(f"The total change in happiness for the optimal seating arrangement would be {findOptimalSeating(table)}.")

    # Setup for part 2
    for name in names:
        table[(name, "Scott")] = 0
    names.add("Scott")
    
    print(f"Inclding myself, the total change in happiness for the optimal seating arrangement would now be {findOptimalSeating(table)}.")