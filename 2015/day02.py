# Day 2: I Was Told There Would Be No Math

# Part 1
def calculateWrappingPaper(present_list: list):
    # Keep a running total of the surface area
    total = 0

    # Loop through the list of presents
    for item in present_list:
        dimensions = sortDimensions(item)

        slack = dimensions[0] * dimensions[1]  # Amount of slack wrapping needed (area of smallest side)
        # Find the total surface area (2*l*w + 2*w*h + 2*h*l) plus the slack
        wrapping_paper = 2 * dimensions[0] * dimensions[1] + 2 * dimensions[0] * dimensions[2] + 2 * dimensions[1] * dimensions[2] + slack

        # Add to running total
        total += wrapping_paper
    
    return total

# Part 2
def calculateRibbonLength(present_list: list):
    # Keep a running total of the ribbon length
    total = 0

    # Loop through the list of presents
    for item in present_list:
        dimensions = sortDimensions(item)

        wrapping = 2 * dimensions[0] + 2 * dimensions[1]  # Amount of ribbon wrapping needed for the present itself (perimeter of smallest face)
        bow = dimensions[0] * dimensions[1] * dimensions[2]  # Amount of ribbon needed for the bow (volume)

        # Add to running total
        total += (wrapping + bow)

    return total

# Helper function for sorting the dimensions of each present
def sortDimensions(item):
    dimensions = item.split("x")  # Split the string based on "x"
    dimensions = [int(dim) for dim in dimensions]  # Convert each string in the list into its integer equivalent
    dimensions.sort()  # Sort the resulting list
    return dimensions


# Example main program
if __name__ == "__main__":
    present_list = []
    print("Enter a list of dimensions in the format '0x0x0', where 0s represent any positive integer. Type 'q' to quit.")

    while True:
        dimension = input()
        if dimension.lower() == "q":
            break
        present_list.append(dimension)
    
    print(f"The elves should order {calculateWrappingPaper(present_list)} square feet of wrapping paper.")  # Part 1
    print(f"In addition, the elves will need to order {calculateRibbonLength(present_list)} feet of ribbon.")  # Part 2