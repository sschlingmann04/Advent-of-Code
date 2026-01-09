# Day 8: Matchsticks

from ast import literal_eval

'''
NOTE: In this file, I am defining the following levels to represent the different forms each string can take. I will use the string "abc" as an example:
    Level 1: The string value itself. In the example, the level 1 string for "abc" would be abc (3 characters).
    Level 2: The string literal as it is represented in code. In the example, the string "abc" (5 characters) is already at level 2, which acts as the base level.
    Level 3: The encoded version of the string if it were to be treated as a raw string. In the example, the level 3 string for "abc" would be "\"abc\"" (9 characters).
'''

# Part 1
def level2_minus_level1(s: str):
    # Convert level 2 string to a level 1 string (can be done easily with the literal_eval() function)
    return len(s) - len(literal_eval(s))  # level 2 string's length - level 1 string's length

# Part 2
def level3_minus_level2(s: str):
    # Convert level 2 string to a level 3 string
    encoded_s = s.replace("\\", "\\\\").replace("\"", "\\\"")  # Replace single backslashes (\) and quotation marks (") with their corresponding escape sequences (\\) (\"), respectively
    encoded_s = "\"" + encoded_s + "\""  # Add quotation marks to the beginning and end of the string
    return len(encoded_s) - len(s)  # level 3 string's length - level 2 string's length


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day8.txt", "r") as f:
            line = f.readline()
            strings = []
            while line:
                strings.append(line.rstrip("\n"))
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")

    diff12, diff23 = 0, 0
    for s in strings:
        diff12 += level2_minus_level1(s)
        diff23 += level3_minus_level2(s)
    
    print(f"The total difference between the number of characters for string literals and the number of characters for their values is {diff12}.")  # Part 1
    print(f"The total difference between the number of characters for the newly encoded strings and the number of characters for the original string literals is {diff23}.")  # Part 2