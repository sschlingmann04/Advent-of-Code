# Day 8: Two-Factor Authentication

# Classes for different types of instructions (for improved readability in the code)
class Rect:
    def __init__(self, w, h):
        self.width = w
        self.height = h

class Rotation:
    def __init__(self, dim, num, shift):
        self.dimension = dim
        self.num = num
        self.shift = shift


# Parts 1 and 2 (result is used for both parts, setup for both parts are in the main program)
def displayScreen(instructions: list):
    # The screen is 50 pixels wide and 6 pixels tall. In this code, a "0" will represent an "off" pixel, while a "1" will represent an "on" pixel.
    screen = [[0 for _ in range(50)] for _ in range(6)]

    for i in instructions:
        # If instruction is to turn on all pixels in a rectangle... set each pixel in the rectangle to 1
        if isinstance(i, Rect):
            for row in range(i.height):
                for col in range(i.width):
                    screen[row][col] = 1
        # If instruction is to rotate a row/column of pixels...
        elif isinstance(i, Rotation):
            # For a row, use slicing to reconstruct the row according to the shift amount
            if i.dimension == "row":
                screen[i.num] = screen[i.num][-i.shift:] + screen[i.num][:-i.shift]
            # For a column, create a new list for that column and copy the values from that list back into the original screen
            elif i.dimension == "column":
                screen_col = [row[i.num] for row in screen]
                screen_col = screen_col[-i.shift:] + screen_col[:-i.shift]
                for index, row in enumerate(screen):
                    row[i.num] = screen_col[index]
            else:
                raise ValueError("Unexpected dimension!")
        
    return screen


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day08.txt", "r") as f:
            line = f.readline()
            instructions = []

            while line:
                if line.startswith("rect"):
                    width, height = line.split()[1].split("x")
                    instructions.append(Rect(int(width), int(height)))
                elif line.startswith("rotate"):
                    split_line = line.split()
                    instructions.append(Rotation(split_line[1], int(split_line[2][2:]), int(split_line[4])))
                else:
                    raise ValueError("Unexpected instruction!")
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")

    screen = displayScreen(instructions)

    # Part 1
    count = 0
    for row in screen:
        count += row.count(1)
    print(f"There are {count} pixels that should be lit after all instructions have ran.")

    # Part 2
    print("...and this is the code the screen is attempting to display:")
    for row in screen:
        for pixel in row:
            if pixel:
                print("#", end="")
            else:
                print(" ", end="")
        print()