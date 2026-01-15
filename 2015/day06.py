# Day 6: Probably a Fire Hazard

# Parts 1 and 2 (determined by the brightness variable)
def setupLights(instruction: str, start: str, end: str, brightness = False):
    start_x, start_y = (int(_) for _ in start.split(","))
    end_x, end_y = (int(_) for _ in end.split(","))

    # Without fine-tuned brightness controls, 1 represents a light that is fully on and 0 represents a light that is fully off
    if not brightness:
        if instruction == "turn on":
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    grid[i][j] = 1

        elif instruction == "turn off":
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    grid[i][j] = 0

        elif instruction == "toggle":
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    grid[i][j] = not grid[i][j]
        
        else:
            raise ValueError("Unexpected instruction!")
    
    # With brightness controls, each digit determines its respective light's brightness level
    else:
        if instruction == "turn on":
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    grid[i][j] += 1

        elif instruction == "turn off":
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    grid[i][j] = grid[i][j] - 1 if grid[i][j] > 0 else 0

        elif instruction == "toggle":
            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    grid[i][j] += 2
        
        else:
            raise ValueError("Unexpected instruction!")


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day06.txt", "r") as f:
            line = f.readline()
            instruction_list = []
            while line:
                instruction_list.append(line)
                line = f.readline()
    except FileNotFoundError:
        print(f"Error: File was not found!")
    
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for inst in instruction_list:
        instruction, start, through, end = inst.rsplit(" ", 3)
        setupLights(instruction, start, end)  # Brightness controls disabled by default
    
    lights_on = 0
    for row in grid:
        for col in row:
            lights_on += col
    
    print(f"Without brightness controls, there are {lights_on} lights that are lit up.")  # Part 1

    grid = [[0 for _ in range(1000)] for _ in range(1000)]  # Resetting grid for part 2
    for inst in instruction_list:
        instruction, start, through, end = inst.rsplit(" ", 3)
        setupLights(instruction, start, end, True)  # This time passing true to enable brightness controls
    
    light_power = 0
    for row in grid:
        for col in row:
            light_power += col
    
    print(f"With brightness controls, the total combined brightness of all lights is {light_power}.")  # Part 2