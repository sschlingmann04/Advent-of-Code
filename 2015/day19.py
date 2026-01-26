# Day 19: Medicine for Rudolph

# Part 1
def findDistinctMolecules(replacements: list, molecule: str):
    distinct_molecules = set()

    for r in replacements:
        for i in range(len(molecule)):
            if molecule[i:i+len(r[0])] == r[0]:
                distinct_molecules.add(molecule[:i] + r[1] + molecule[i+len(r[0]):])
    
    return distinct_molecules

# Part 2
def fabricateMolecule(replacements: list, molecule: str):
    # Base case: if we reduce the molecule all the way down to "e" then we are done
    if molecule == "e":
        return 0

    # Greedy algorithm: among the possible replacements, always choose the one that gives the shortest string
    possible_replacements = set()
    for r in replacements:
        for i in range(len(molecule)):
            if molecule[i:i+len(r[1])] == r[1]:
                possible_replacements.add(molecule[:i] + r[0] + molecule[i+len(r[1]):])
    
    return 1 + fabricateMolecule(replacements, min(possible_replacements, key=len)) if len(possible_replacements) is not 0 else 1


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day19.txt", "r") as f:
            line = f.readline()
            replacements = []

            while line != "\n":
                first, second = line.split(" => ")
                replacements.append((first, second.strip()))
                line = f.readline()
            
            molecule = f.readline().strip()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"{len(findDistinctMolecules(replacements, molecule))} distinct molecules can be created.")  # Part 1
    print(f"It will take at minimum {fabricateMolecule(replacements, molecule)} steps to go from \"e\" to the original medicine molecule.")  # Part 2
    # NOTE: Part 2 unfortunately does NOT return the correct solution on every run due to how strings are added to the set and the possibility of ties with the lengths