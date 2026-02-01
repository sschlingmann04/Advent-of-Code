# Day 25: Let It Snow

# Part 1 (the only part)
def getCode(row: int, col: int):
    # Start by finding out how many iterations of the formula would be needed to get to this location on the grid
    steps = int((row + col - 2) * (row + col - 1) / 2 + col)

    # From given data, we know the bottom-right most cell (6,6) on the revealed portion of the grid is the place we should start. Get the number of iterations needed to get here
    start_step = int((10 * 11) / 2 + 6)  # 6 + 6 - 2 = 10, 6 + 6 - 1 = 11 (both using the formula above)

    value = 27995004  # Value contained in (6,6) in the given data
    for i in range(start_step, steps):
        value = value * 252533 % 33554393  # Given formula from the problem
    
    return value


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day25.txt", "r") as f:
            row, col = [int(x[:-1]) for x in f.read().split() if x[:-1].isnumeric()]
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"The machine should be given the value {getCode(row, col)} as the code. Happy holidays!")  # Part 1 (the only part)