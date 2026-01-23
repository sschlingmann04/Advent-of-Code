# Day 17: No Such Thing as Too Much

from inspect import stack

# Parts 1 and 2 (function returns all values needed for both parts)
def numCombinations(containers: list, liters: int):
    total_combinations = 0
    global min_containers_used, min_container_combos

    for i in range(len(containers)):
        liters_remaining = liters - containers[i]
        if liters_remaining > 0:
            total_combinations += numCombinations(containers[i+1:], liters_remaining)[0]  # Index 0 references the first returned value
        elif liters_remaining == 0:
            # Gets the current depth of the call stack and subtracts 1 from it (to account for the main function). This represents the number of containers used in this combo.
            containers_used = len(stack()) - 1
            total_combinations += 1
            # If the number of containers used in this combination is less than the absolute minimum used in any prior combination, then update the minimum
            if containers_used < min_containers_used:
                min_containers_used = containers_used
                min_container_combos = 1  # Reset the count of combinations for the miniumum amount of containers to 1
            elif containers_used == min_containers_used:
                min_container_combos += 1
    
    return total_combinations, min_containers_used, min_container_combos
    

# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day17.txt", "r") as f:
            line = f.readline()
            containers = []
            while line:
                containers.append(int(line))
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    min_containers_used = len(containers)
    min_container_combos = 0

    liters = 150
    combos, min_containers, min_combos = numCombinations(containers, liters)
    print(f"There are {combos} total combinations of containers that can fit all {liters} liters of eggnog.")  # Part 1
    print(f"However, by using the minimum amount of containers necessary ({min_containers}), there are {min_combos} combinations that use that many containers.")  # Part 2