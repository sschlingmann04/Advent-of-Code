# Day 23: Opening the Turing Lock

# Parts 1 and 2 (determined by the registers variable)
def runProgram(instructions: list[list], registers: dict[str, int]):
    x = 0  # Represents the instruction that should run next
    while True:
        try:
            curr_inst = instructions[x]
            opcode = curr_inst[0]
            # "hlf r" sets register r to half its current value and moves to the next instruction
            if opcode == "hlf":
                r = curr_inst[1]
                registers[r] /= 2
                x += 1
            # "tpl r" sets register r to triple its current value and moves to the next instruction
            elif opcode == "tpl":
                r = curr_inst[1]
                registers[r] *= 3
                x += 1
            # "inc r" adds 1 to register r and moves to the next instruction
            elif opcode == "inc":
                r = curr_inst[1]
                registers[r] += 1
                x += 1
            # "jmp offset" jumps to the instruction offset away from itself
            elif opcode == "jmp":
                offset = curr_inst[1]
                x += offset
            # "jie r, offset" only jumps to the instruction offset away from itself if register r is even
            elif opcode == "jie":
                r, offset = curr_inst[1], curr_inst[2]
                if registers[r] % 2 == 0:
                    x += offset
                else:
                    x += 1
            # "jio r, offset" only jumps to the instruction offset away from itself if register r is 1
            elif opcode == "jio":
                r, offset = curr_inst[1], curr_inst[2]
                if registers[r] == 1:
                    x += offset
                else:
                    x += 1
            else:
                raise ValueError("Unexpected operation code!")
        
        # If the pointer to the next instruction is out of bounds, this will catch the exception and break out of the loop
        except IndexError:
            break
    
    return registers


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day23.txt", "r") as f:
            line = f.readline()
            instructions = []
            while line:
                split_line = line.split()

                # "ji" means "jump if" and tests for either a "jie" or "jio" instruction, both of which contain the string "ji"
                if "ji" in split_line[0]:
                    split_line[1] = split_line[1].strip(",")
                    split_line[2] = int(split_line[2])
                elif split_line[0] == "jmp":
                    split_line[1] = int(split_line[1])
                
                instructions.append(split_line)
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    registers = runProgram(instructions, {"a": 0, "b": 0})
    print(f"After execution of the program with register a starting at 0, {registers["b"]} is the value contained within register b.")  # Part 1

    registers = runProgram(instructions, {"a": 1, "b": 0})
    print(f"After execution of the program with register a starting at 1, {registers["b"]} is the value contained within register b.")  # Part 2
    
    '''NOTE: The given instructions are secretly hiding an interpretation of the Collatz conjecture.
        The Collatz conjecture states that by starting at any integer, if you halve it when its even and triple it plus add 1 when its odd, you will always eventually arrive at 1.
        In action, this looks like this:
            Line 42 checks if a is 1, then jumps to line 50 if true. Since line 50 does not exist, this effectively ends the program when a is 1.
            Line 43 increments the value of b by 1. This effectively counts the amount of times the loop is performed.
            Line 44 handles the case when a is even. It jumps to line 48 and halves a.
            Lines 45 and 46 handle the case when a is odd. It triples the value of a and then adds 1 to it. Then, line 47 jumps over line 48 to ensure that actiom is not done.
            Finally, both control flows eventually reach line 49, which jumps back to line 42 and starts the loop all over again.
        Lines 1-41 just set a to an arbitrary integer to start with. Lines 1, 20-41 run when a is 1, and lines 2-19 run when a is not 1 (or in this case, when a is 0).

    Pretty cool observation when you finally see it for the first time!'''