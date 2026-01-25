# Day 18: Like a GIF For Your Yard

# Helper function to count the number of neighboring lights that are on in the (up to) 8 surrounding cells
def getOnNeighbors(grid: list, row: int, col: int):
    on_neighbors = 0

    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            # Don't check the middle cell (i.e. the cell itself) or any cell out of bounds (negative indexes will loop around to the other side)
            if (r == row and c == col) or (r < 0 or c < 0):
                continue
            try:
                if grid[r][c] == "#":
                    on_neighbors += 1
            except IndexError:
                continue
    
    return on_neighbors


# Parts 1 and 2 (determined by the "stuck_lights" variable)
def conwaysGameOfLife(grid: list, steps: int, stuck_lights: list = []):
    for n in range(steps):
        next_grid = []

        for row in range(len(grid)):
            next_grid.append("")
            for col in range(len(grid[row])):
                on_neighbors = getOnNeighbors(grid, row, col)

                '''If any of the following conditions are met the light should be on in the next cycle:
                    1. There are exactly 3 neighboring lights that are on, regardless of whether the light was on or off previously.
                    2. There are exactly 2 neighboring lights that are on AND the light was already on previously.
                    3. The light is one of the designated "stuck lights", i.e. they are permanently on and cannot be turned off.'''
                if on_neighbors == 3 or (on_neighbors == 2 and grid[row][col] == "#") or (row, col) in stuck_lights:
                    next_grid[row] += "#"
                
                # Anything else and the light should be off
                else:
                    next_grid[row] += "."
               
        grid = next_grid

    # Count all on lights in the final grid and return the result
    on_lights = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "#":
                on_lights += 1
    
    return on_lights


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day18.txt", "r") as f:
            line = f.readline().strip()
            grid = []
            while line:
                grid.append(line)
                line = f.readline().strip()
    except FileNotFoundError:
        print("Error: File was not found!")

    steps = 100
    on = conwaysGameOfLife(grid, steps)
    print(f"There are {on} lights on after {steps} steps.")  # Part 1

    # For part 2, the "stuck lights" are designated as the 4 corner lights
    stuck_lights = [(0, 0), (0, len(grid) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid) - 1)]
    on = conwaysGameOfLife(grid, steps, stuck_lights)
    print(f"However, if the four corner lights are left permanently on, there are actually {on} lights on after {steps} steps.")  # Part 2