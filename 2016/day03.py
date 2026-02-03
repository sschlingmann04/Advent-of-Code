# Day 3: Squares With Three Sides

# Helper function for part 2
def rearrangeTriangles(triangles: list[list[int]]):
    new_triangles = []

    # For every block of three triangles, rearrange them so that they are added by columns into the new_triangles list
    for tri in range(0, len(triangles), 3):
        for i in range(0, 3):
            new_triangles.append(sorted([triangles[tri][i], triangles[tri+1][i], triangles[tri+2][i]]))
    
    return new_triangles


# Parts 1 and 2 (only the input changes between parts)
def countValidTriangles(triangles: list[list[int]]):
    return len([tri for tri in triangles if tri[0] + tri[1] > tri[2]])  # A triangle is only valid if the sum of its two shortest sides is larger than its longest side


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day03.txt", "r") as f:
            triangles = [[int(num) for num in line.split()] for line in f.readlines()]
    except FileNotFoundError:
        print("Error: File was not found!")
    
    triangles_by_row = [sorted(tri) for tri in triangles]
    print(f"Of the listed triangles in their default arrangement (by row), {countValidTriangles(triangles_by_row)} are possible.")  # Part 1

    triangles_by_col = rearrangeTriangles(triangles)
    print(f"Of the listed triangles in a vertical arrangement (by col), {countValidTriangles(triangles_by_col)} are possible.")  # Part 2