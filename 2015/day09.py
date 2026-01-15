# Day 9: All in a Single Night

from math import inf
from itertools import permutations

# Part 1
def findShortestPath(graph: dict):
    # Get all possible permutations of routes that can be traversed
    all_routes = list(permutations(graph.keys()))
    shortest_path = inf
    current_path = 0

    # Loop through each possible route
    for route in all_routes:
        # Loop through each city in the route (-1 is there so that an index is not accessed out of bounds later when trying to access the next city)
        for city in range(len(route) - 1):
            # Loop through each possible path to another city that can be reached from the current city in the graph
            for path in range(len(graph[route[city]])):
                # If the city on this path ([0] to access the city name) is equal to the next city in the route (i.e. from the current city to the next city along the route)
                if graph[route[city]][path][0] == route[city + 1]:
                    current_path += graph[route[city]][path][1]  # Add the distance to the next city ([1] to access the distance) to the current_path variable
                    break  # Break out of the inner loop since we have found the correct tuple in the graph and move onto the next city on the route
        
        # Update the shortest_path variable if the current_path is smaller than it and reset the current_path back to 0
        shortest_path = min(shortest_path, current_path)
        current_path = 0
    
    return shortest_path

# Part 2
def findLongestPath(graph: dict):
    # Get all possible permutations of routes that can be traversed
    all_routes = list(permutations(graph.keys()))
    longest_path = 0
    current_path = 0

    # Loop through each possible route
    for route in all_routes:
        # Loop through each city in the route (-1 is there so that an index is not accessed out of bounds later when trying to access the next city)
        for city in range(len(route) - 1):
            # Loop through each possible path to another city that can be reached from the current city in the graph
            for path in range(len(graph[route[city]])):
                # If the city on this path ([0] to access the city name) is equal to the next city in the route (i.e. from the current city to the next city along the route)
                if graph[route[city]][path][0] == route[city + 1]:
                    current_path += graph[route[city]][path][1]  # Add the distance to the next city ([1] to access the distance) to the current_path variable
                    break  # Break out of the inner loop since we have found the correct tuple in the graph and move onto the next city on the route
        
        # Update the longest_path variable if the current_path is larger than it and reset the current_path back to 0
        longest_path = max(longest_path, current_path)
        current_path = 0
    
    return longest_path


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day09.txt", "r") as f:
            line = f.readline()
            graph = {}
            while line:
                locations, distance = line.split(" = ")
                distance = int(distance)
                start, end = locations.split(" to ")

                if graph.get(start) is not None:
                    graph[start].append((end, distance))
                else:
                    graph[start] = [(end, distance)]
                if graph.get(end) is not None:
                    graph[end].append((start, distance))
                else:
                    graph[end] = [(start, distance)]
                
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"The distance of the shortest route in the network is {findShortestPath(graph)}.")  # Part 1
    print(f"The distance of the longest route in the network is {findLongestPath(graph)}.")  # Part 2