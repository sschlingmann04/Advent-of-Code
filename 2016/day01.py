# Day 1: No Time for a Taxicab

# Parts 1 and 2 (determined by the repeat_visit variable)
def findShortestPath(directions: list[str], no_repeat_visit = False):
    cardinal = ["N", "E", "S", "W"]
    street_grid = {"N": 0, "E": 0, "S": 0, "W": 0}
    visited = [(0, 0)]  # Only relevant for part 2
    repeat_found = False  # Only relevant for part 2
    facing_direction = cardinal[0]  # Start by facing north (N)

    for dir in directions:
        index = cardinal.index(facing_direction)
        # right (R) moves us forward in the cardinal list of directions, left (L) moves us backward
        if dir.startswith("R"):
            facing_direction = cardinal[(index + 1) % 4]
        elif dir.startswith("L"):
            facing_direction = cardinal[(index - 1)]
        else:
            raise ValueError("Unexpected character!")
        
        num_blocks = int(dir[1:])

        # Only relevant for part 2, where the destination is the first block visited twice
        if no_repeat_visit:
            x, y = visited[-1]  # x and y are set to the current/most recent block on the street grid

            for i in range(1, num_blocks + 1):
                street_grid[facing_direction] += 1
                if facing_direction == "N":
                    next_block = (x, y + i)
                elif facing_direction == "E":
                    next_block = (x + i, y)
                elif facing_direction == "S":
                    next_block = (x, y - i)
                elif facing_direction == "W":
                    next_block = (x - i, y)
                else:
                    raise ValueError("Unexpected direction!")

                # If the next block has already been visited, then do not search any further. The repeat_found variables ensures the outer for loop is exited as well
                if next_block in visited:
                    repeat_found = True
                    break
                
                # Otherwise add this block to the list of visited blocks
                visited.append(next_block)
            
            # Outer loop should be exited as well if a previously visited block is discovered
            if repeat_found:
                break
        
        # Otherwise, just add the number of blocks as a net amount travelled in that direction
        else:
            street_grid[facing_direction] += num_blocks
    
    # The shortest Manhattan distance is the net horizontal distance added to the net vertical distance
    return abs(street_grid["E"] - street_grid["W"]) + abs(street_grid["N"] - street_grid["S"])


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day01.txt", "r") as f:
            directions = f.read().split(", ")
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"Easter Bunny HQ is {findShortestPath(directions)} blocks away.")  # Part 1
    print(f"The first location visited twice is {findShortestPath(directions, no_repeat_visit=True)} blocks away.")  # Part 2