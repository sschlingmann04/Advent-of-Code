# Day 2: Bathroom Security

# Parts 1 and 2 (determined by the keypad variable)
def getBathroomCode(instructions: list[str], keypad: list[list], start_pos):
    # Start by getting the row and col of the starting button on the keypad
    row, col = (None, None)
    for r in keypad:
        if start_pos in r:
            row = keypad.index(r)
            col = r.index(start_pos)
            break   
    if not row:
        raise LookupError("Starting buttton was not found on the given keypad!")
    
    code = []

    # Loop through each character in each line of the instructions
    for line in instructions:
        for char in line:
            # Lookup table
            dx, dy = {
                "U": (-1, 0),
                "D": (1, 0),
                "L": (0, -1),
                "R": (0, 1)
            }[char]

            # Check if the keypad position we are jumping to is out of bounds (either explicitly or implicitly with None for an irregularly-shaped keypad as in part 2)
            try:
                assert keypad[row+dx][col+dy] and row+dx >= 0 and col+dy >= 0
            except:
                continue

            # Update row and col indices if they lead to a valid position on the keypad
            row += dx
            col += dy
        
        # Add whatever keypad character we're on after each line (as a string for the join at the end)
        code.append(str(keypad[row][col]))
    
    return "".join(code)


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day02.txt", "r") as f:
            instructions = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: File was not found!")
    
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"With the first keypad, {getBathroomCode(instructions, keypad, 5)} is the bathroom code.")  # Part 1

    keypad2 = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None]
    ]
    print(f"With the second keypad, {getBathroomCode(instructions, keypad2, 5)} is the bathroom code.")  # Part 2