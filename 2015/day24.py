# Day 24: It Hangs in the Balance

from itertools import product
from math import inf

# Parts 1 and 2 (determined by the groups variable)
def findIdealQuantumEntanglement(weights: list[int], groups: int):
    # Get the weight per group (sum of all weights divided by the number of groups)
    weight_per_group = int(sum(weights) / groups)
    package_count = 0
    ideal_configs = []

    # Find only the configurations with the smallest package count that sum to the proper group weight (calculated above)
    while len(ideal_configs) == 0:
        package_count += 1
        ideal_configs = [x for x in product(weights, repeat=package_count) if sum(x) == weight_per_group and len(set(x)) == len(x)]

    # Find the quantum entanglement of each configuration and return the lowest one
    QE = inf
    for i in ideal_configs:
        current_QE = 1
        for num in i:
            current_QE *= num
        QE = min(current_QE, QE)
    
    return QE


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day24.txt", "r") as f:
            weights = [int(num) for num in f.readlines()]
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"In the ideal configuration with 3 groups, {findIdealQuantumEntanglement(weights, 3)} is the quantum entanglement (QE) of the first group of packages.")
    print(f"In the ideal configuration with 4 groups, {findIdealQuantumEntanglement(weights, 4)} is the quantum entanglement (QE) of the first group of packages.")