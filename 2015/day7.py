# Day 7: Some Assembly Required

# Parts 1 and 2 (setup for part 2 is in the main program)
def assembleCircuit(instruction: str, output: str):
    if "AND" in instruction:
        lhs, rhs = instruction.split(" AND ")  # Get the left and right hand sides of the instruction

        # If either side is numeric, convert it to an integer
        if lhs.isnumeric():
            lhs = int(lhs)
        
        # If either side's variable's value is not in the lookup table, then it hasn't been calculated yet
        elif lookup_table.get(lhs) is None:
            lhs = assembleCircuit(circuit.get(lhs), lhs)
        
        # Otherwise, it is in the lookup table and we can replace the variable with its value
        else:
            lhs = lookup_table.get(lhs)

        # Repeat for the right hand side variable
        if rhs.isnumeric():
            rhs = int(rhs)
        elif lookup_table.get(rhs) is None:
            rhs = assembleCircuit(circuit.get(rhs), rhs)
        else:
            rhs = lookup_table.get(rhs)
        
        # Once both values are determined, perform the AND operation
        result = lhs & rhs
    
    elif "OR" in instruction:
        lhs, rhs = instruction.split(" OR ")  # Get the left and right hand sides of the instruction

        # If either side is numeric, convert it to an integer
        if lhs.isnumeric():
            lhs = int(lhs)
        
        # If either side's variable's value is not in the lookup table, then it hasn't been calculated yet
        elif lookup_table.get(lhs) is None:
            lhs = assembleCircuit(circuit.get(lhs), lhs)
        
        # Otherwise, it is in the lookup table and we can replace the variable with its value
        else:
            lhs = lookup_table.get(lhs)

        # Repeat for the right hand side variable
        if rhs.isnumeric():
            rhs = int(rhs)
        elif lookup_table.get(rhs) is None:
            rhs = assembleCircuit(circuit.get(rhs), rhs)
        else:
            rhs = lookup_table.get(rhs)
        
        # Once both values are determined, perform the OR operation
        result = lhs | rhs
    
    elif "NOT" in instruction:
        var = instruction.lstrip("NOT ")  # Strip off "NOT " to just get the variable/value

        # If var is numeric, convert it to an integer
        if var.isnumeric():
            var = int(var)
        
        # If var is not in the lookup table, then it hasn't been calculated yet
        elif lookup_table.get(var) is None:
            var = assembleCircuit(circuit.get(var), var)
        
        # Otherwise, it is in the lookup table and we can replace the variable with its value
        else:
            var = lookup_table.get(var)
        
        # Once var has been determined, perform the NOT operation and use a 0xFFFF mask to treat the result as an unsigned 16-bit integer
        result = (~var) & 0xFFFF
    
    elif "LSHIFT" in instruction:
        lhs, rhs = instruction.split(" LSHIFT ")  # Get the left and right hand sides of the instruction

        # If the left hand side is numeric, convert it to an integer
        if lhs.isnumeric():
            lhs = int(lhs)
        
        # If the left hand side's variable's value is not in the lookup table, then it hasn't been calculated yet
        elif lookup_table.get(lhs) is None:
            lhs = assembleCircuit(circuit.get(lhs), lhs)
        
        # Otherwise, it is in the lookup table and we can replace the variable with its value
        else:
            lhs = lookup_table.get(lhs)

        # The right hand side is guaranteed to be numeric so we can convert it immediately
        rhs = int(rhs)
        
        # Once both values are determined, perform the LEFT SHIFT
        result = lhs << rhs
    
    elif "RSHIFT" in instruction:
        lhs, rhs = instruction.split(" RSHIFT ")  # Get the left and right hand sides of the instruction

        # If the left hand side is numeric, convert it to an integer
        if lhs.isnumeric():
            lhs = int(lhs)
        
        # If the left hand side's variable's value is not in the lookup table, then it hasn't been calculated yet
        elif lookup_table.get(lhs) is None:
            lhs = assembleCircuit(circuit.get(lhs), lhs)
        
        # Otherwise, it is in the lookup table and we can replace the variable with its value
        else:
            lhs = lookup_table.get(lhs)

        # The right hand side is guaranteed to be numeric so we can convert it immediately
        rhs = int(rhs)
        
        # Once both values are determined, perform the RIGHT SHIFT
        result = lhs >> rhs

    # Base case 1: the "instruction" is a number
    elif instruction.isnumeric():
        result = int(instruction)
    
    # Base case 2: the "instruction" is a variable
    else:
        result = assembleCircuit(circuit.get(instruction), instruction)

    # Add result to lookup table and return the result
    lookup_table[output] = result
    return result


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day7.txt", "r") as f:
            line = f.readline()
            circuit = {}
            while line:
                instruction, output = line.split(" -> ")
                output = output.rstrip("\n")
                circuit[output] = instruction
                line = f.readline()
    except FileNotFoundError:
        print(f"Error: File was not found!")
    
    lookup_table = {}
    a = assembleCircuit(circuit.get("a"), "a")
    print(f"The signal that is provided to wire a is {a}.")  # Part 1

    # Setup for part 2
    circuit["b"] = str(a)  # Override wire b with wire a's signal
    lookup_table.clear()  # Reset all other wires
    a = assembleCircuit(circuit.get("a"), "a")
    print(f"After overriding wire b with the previous signal and resetting the circuit, the new signal provided to wire a is {a}.")  # Part 2