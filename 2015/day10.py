# Day 10: Elves Look, Elves Say

# Parts 1 and 2 (determined by the iterations variable)
def look_and_say(input: str, iterations: int):
    for i in range(iterations):
        new_input = ""
        current_digit = input[0]
        count = 0

        for c in input:
            if c == current_digit:
                count += 1
            else:
                new_input += str(count) + current_digit
                current_digit = c
                count = 1
        
        new_input += str(count) + current_digit
        input = new_input
    
    return input


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day10.txt", "r") as f:
            input = f.read()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"The length of the result after 40 iterations of the look-and-say sequence on {input} is {len(look_and_say(input, 40))}.")
    print(f"After 50 iterations on the same input, the length of the result is {len(look_and_say(input, 50))}.")