# Day 3: Perfectly Spherical Houses in a Vacuum

# Parts 1 and 2 (determined by the santa_count variable)
def countUniqueHouses(directions: str, santa_count: int):
    # Initialize variables
    coordinates = []
    for i in range(santa_count):
        coordinates.append([0, 0])  # List will contain x subset lists, with x being the number of Santas and each subset list tracking its respective Santa's position
    grid = [(0, 0)]
    houses = 1
    pos = 0  # Determines which Santa to move

    # Loop through string and process each direction movement
    for char in directions:
        # Assign variables x and y for cleaner code
        x = coordinates[pos][0]
        y = coordinates[pos][1]

        if char == ">":
            x += 1
        elif char == "<":
            x -= 1
        elif char == "^":
            y += 1
        elif char == "v":
            y -= 1
        else:
            raise ValueError("Unexpected character!")
        
        # If coordinate is not in grid, then this house has not been visited previously
        if (x, y) not in grid:
            grid.append((x, y))  # Add it to the grid
            houses += 1  # Increment the count of unique houses visited
        
        # Update original coordinates list with the values of x and y
        coordinates[pos][0] = x
        coordinates[pos][1] = y
        
        # Move pos variable to the next Santa; if at the end then recycle back to the beginning
        if pos == santa_count - 1:
            pos = 0
        else:
            pos += 1
    
    return houses


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day3.txt", "r") as f:
            directions = f.read()
    except FileNotFoundError:
        print(f"Error: File was not found!")

    print(f"{countUniqueHouses(directions, 1)} houses will receive at least one present with one Santa doing all the work himself.")
    print(f"With Robo-Santa included, {countUniqueHouses(directions, 2)} houses will receive at least one present.")