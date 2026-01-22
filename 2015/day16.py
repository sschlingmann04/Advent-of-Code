# Day 16: Aunt Sue

# Part 1
def findCorrectSue(sues: dict, target: dict):
    # Generate a list of all attributes (the keys)
    atts = list(target.keys())

    # Start at index 1 instead of 0 (the 0th index is a "dummy" index)
    for i in range(1, len(sues)):
        matches = 0
        for att in atts:
            if sues[i][att] == None:  # If the value is None then it doesn't count
                continue
            elif sues[i][att] == target[att]:  # If the value assigned to the attribute matches our target value for that same attribute, we found a match!
                matches += 1
            else:  # If, however, the value assigned to the attribute is not None but also does not match, this is not the Sue we are looking for
                break
            
            # If we found 3 matches then we found the right Sue
            if matches == 3:
                return i
    
    # If we never found the correct Sue...
    return -1

# Part 2
def findTheRealSue(sues: dict, target: dict):
    # Generate a list of all attributes (the keys)
    atts = list(target.keys())

    # Start at index 1 instead of 0 (the 0th index is a "dummy" index)
    for i in range(1, len(sues)):
        matches = 0
        for att in atts:
            if sues[i][att] == None:  # If the value is None then it doesn't count
                continue
            
            # If the attribute we are checking is for cats or trees, it should be interpreted as needing to be greater than the target value
            if att == "cats" or att == "trees":
                if sues[i][att] > target[att]:
                    matches += 1
                else:
                    break
            
            # If the attribute we are checking for is pomeranians or goldfish, it should be interpreted as needing to be lesser than the target value
            elif att == "pomeranians" or att == "goldfish":
                if sues[i][att] < target[att]:
                    matches += 1
                else:
                    break

            # All other attributes should be interpreted as needing to be equal to the target value
            else:
                if sues[i][att] == target[att]:
                    matches += 1
                else:
                    break
            
            # If we found 3 matches then we found the right Sue
            if matches == 3:
                return i
    
    # If we never found the correct Sue...
    return -1


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day16.txt", "r") as f:
            line = f.readline()
            
            # Create a base "attributes" dictionary and assign None to each value. This will also serve as the 0th index to the "sues" list
            attributes = {
                "children": None,
                "cats": None,
                "samoyeds": None,
                "pomeranians": None,
                "akitas": None,
                "vizslas": None,
                "goldfish": None,
                "trees": None,
                "cars": None,
                "perfumes": None
            }
            sues = [attributes.copy() for _ in range(501)]  # 501 instead of 500 so the indexes can match up with the actual "Sue" numbers
            index = 1  # Starting at index 1 for the same reason so the 0th index is not modified

            while line:
                # Split the line by spaces and trim off the last character unless it is the first or last item in the list
                split_line = [line.split()[i][:-1] if 0 < i < len(line.split()) - 1 else line.split()[i] for i in range(len(line.split()))]
                # Start at index 2 (indexes 0 and 1 are irrelevant) and step 2 indexes at a time
                for i in range(2, len(split_line), 2):
                    sues[index][split_line[i]] = int(split_line[i + 1])
                
                index += 1
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")

    target_dict = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    print(f"Sue {findCorrectSue(sues, target_dict)} is the one that sent the gift.")  # Part 1
    print(f"After noticing the outdated retroencabulator, it turns out that Sue {findTheRealSue(sues, target_dict)} is actually the one that sent the gift.")  # Part 2