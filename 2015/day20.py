# Day 20: Infinite Elves and Infinite Houses

from math import floor, sqrt, inf

# Parts 1 and 2 (determined by the scale and house_limit variables)
def calculatePresents(house_num, scale, house_limit = inf):
    # Problem can be reduced to simply finding the factors of the house number
    factors = set()

    # Search all integers starting from 1 for possible factors (no need to search past the square root)
    for i in range(1, floor(sqrt(house_num)) + 1):
        # If number is divisible by i...
        if house_num % i == 0:
            # Only add i as a possible factor if the house number divided by it is less than or equal to the house limit
            if house_num / i <= house_limit:
                factors.add(i)
            # Only add i's counterpart as a possible factor if i itself is less than or equal to the house limit
            if i <= house_limit:
                factors.add(house_num / i)
    
    # Sum all possible factors and multiply by the given scale
    return int(sum(factors)) * scale


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day20.txt", "r") as f:
            num = int(f.read())
    except FileNotFoundError:
        print("Error: File was not found!")
    
    for i in range(1, num):
        if calculatePresents(i, 10) >= num:
            print(f"With an infinite limit of houses per elf and a scale of 10, house {i} is the lowest-numbered house to receive at least {num} presents.")  # Part 1
            break
    
    for i in range(1, num):
        if calculatePresents(i, 11, 50) >= num:
            print(f"With a limit of 50 houses per elf and a scale of 11, house {i} is the lowest-numbered house to receive at least {num} presents.")  # Part 2
            break