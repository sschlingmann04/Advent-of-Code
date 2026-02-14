# Day 10: Balance Bots

# Parts 1 and 2 (different parts of the result are used for both parts, setup for both parts are in the main program)
def runBotFactory(value_instructions: list[list[int]], bot_instructions: dict[int, list], max_bot_num: int, max_output_num: int):
    bots = [[] for _ in range(max_bot_num + 1)]
    outputs = [None for _ in range(max_output_num + 1)]
    # For the purposes of this function, a "ready bot" is defined as any bot that has its two microochips and can thus pass them off to other bots/outputs
    ready_bots = []  # Stores the numbers of any bots that are ready
    already_executed = set()  # Stores the numbers of any bots that have already executed their instruction

    # Start by executing all value instructions (i.e. instructions that directly assign a value to a bot)
    for value_inst in value_instructions:
        value, bot_num = value_inst
        bots[bot_num].append(value)
        if len(bots[bot_num]) == 2:
            ready_bots.append(bot_num)
    
    # Continue to execute bot instructions as long as there is at least one ready bot
    while ready_bots:
        bot_num = ready_bots[0]
        low_type, low_num, high_type, high_num = bot_instructions[bot_num]

        if low_type == "bot":
            bots[low_num].append(min(bots[bot_num]))
            if low_num not in already_executed and len(bots[low_num]) == 2:
                ready_bots.append(low_num)
        elif low_type == "output":
            outputs[low_num] = min(bots[bot_num])
        
        if high_type == "bot":
            bots[high_num].append(max(bots[bot_num]))
            if high_num not in already_executed and len(bots[high_num]) == 2:
                ready_bots.append(high_num)
        elif high_type == "output":
            outputs[high_num] = max(bots[bot_num])
        
        already_executed.add(bot_num)
        ready_bots.remove(bot_num)
    
    return bots, outputs


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day10.txt", "r") as f:
            value_instructions = []
            bot_instructions = {}
            max_bot_num, max_output_num = 0, 0
            line = f.readline()

            while line:
                split_line = line.split()

                # Value instruction
                if split_line[0] == "value":
                    '''
                    After split:
                        value x goes to bot y
                          ^   ^   ^   ^  ^  ^
                          0   1   2   3  4  5 (indices)
                    '''
                    # Index 1 corresponds to the value and index 5 corresponds to the bot number the value should go to
                    value, bot_num = int(split_line[1]), int(split_line[5])
                    value_instructions.append([value, bot_num])
                    max_bot_num = max(max_bot_num, bot_num)
                # Bot instruction
                elif split_line[0] == "bot":
                    '''
                    After split:
                        bot x gives low to bot/output y and high to bot/output z
                         ^  ^   ^    ^   ^    ^       ^  ^    ^   ^     ^^     ^^
                         0  1   2    3   4    5       6  7    8   9     10     11 (indices)
                    '''
                    # Index 1 corresponds to the bot, indexes 5-6 tell where the low value should go to, and indexes 10-11 tell where the high value should go to
                    bot_num, low_type, low_num, high_type, high_num = int(split_line[1]), split_line[5], int(split_line[6]), split_line[10], int(split_line[11])
                    bot_instructions[bot_num] = [low_type, low_num, high_type, high_num]

                    if low_type == "bot":
                        max_bot_num = max(max_bot_num, low_num)
                    elif low_type == "output":
                        max_output_num = max(max_output_num, low_num)
                    else:
                        raise ValueError("Unexpected output type!")

                    if high_type == "bot":
                        max_bot_num = max(max_bot_num, high_num)
                    elif high_type == "output":
                        max_output_num = max(max_output_num, high_num)
                    else:
                        raise ValueError("Unexpected output type!")
                else:
                    raise ValueError("Unexpected instruction!")

                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    bots, outputs = runBotFactory(value_instructions, bot_instructions, max_bot_num, max_output_num)
    
    # Part 1
    num1, num2 = 61, 17
    for index, b in enumerate(bots):
        if num1 in b and num2 in b:
            print(f"Bot {index} is responsible for comparing value-{num1} microchips with value-{num2} microchips.")
            break
    
    # Part 2
    print(f"By multiplying the values of the chips in outputs 0, 1, and 2, {outputs[0] * outputs[1] * outputs[2]} becomes the result.")