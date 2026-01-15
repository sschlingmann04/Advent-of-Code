# Day 1: Not Quite Lisp

# Part 1
def findFloor(directions):
    return directions.count("(") - directions.count(")")

# Part 2
def findBasementEntry(directions):
    for i in range(len(directions)):
        if findFloor(directions[:i+1]) == -1:
            return i + 1
    return -1
    

# Example main program
if __name__ == "__main__":
    directions = "(())()()((((()(()())(((((())))())))())()))()())"
    print(f"Instructions take Santa to floor {findFloor(directions)}.")  # Part 1, answer for example would be -1
    print(f"Basement is first entered at position {findBasementEntry(directions)}.")  # Part 2, answer for example would be 47 (the last character)