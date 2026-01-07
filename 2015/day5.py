# Day 5: Doesn't He Have Intern-Elves For This?

# Part 1
def isNiceString(s: str):
    # If less than three vowels, string is not nice
    if s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") < 3:
        return False
    
    # If string contains "ab", "cd", "pq", or "xy", it is not nice
    if s.find("ab") != -1 or s.find("cd") != -1 or s.find("pq") != -1 or s.find("xy") != -1:
        return False
    
    # If no consecutive letters, string is not nice
    last_char = ""
    for c in s:
        if c == last_char:
            return True
        last_char = c

    # If we made it to the end and did not exit from the loop early, then no consecutive letters were found and the string is not nice
    return False

# Part 2
def isNiceString2(s: str):
    condition1, condition2 = False, False

    for i in range(len(s) - 2):
        # Condition 1: If string does not contain a repeated non-overlapping pair of letters, it is not nice
        if not condition1 and i != len(s) - 2 and s.find(s[i:i+2], i + 2) != -1:
            condition1 = True
        # Condition 2: If string does not contain repeated letters separated by a letter between them, it is not nice
        if not condition2 and s[i] == s[i+2]:
            condition2 = True
        # If both conditions have been satisfied, the string is nice and we can exit the loop
        if condition1 and condition2:
            return True

    # If we made it to the end and did not exit from the loop early, at least one condition was not satisfied and the string is not nice
    return False


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day5.txt", "r") as f:
            line = f.readline()
            strings = []
            while line:
                strings.append(line)
                line = f.readline()
    except FileNotFoundError:
        print(f"Error: File was not found!")
    
    nice_count = 0
    nice_count2 = 0
    for s in strings:
        if isNiceString(s):
            nice_count += 1
        if isNiceString2(s):
            nice_count2 += 1
    
    print(f"There are {nice_count} nice strings under the original ruleset.")  # Part 1
    print(f"There are {nice_count2} nice strings under the modified ruleset.")  # Part 2