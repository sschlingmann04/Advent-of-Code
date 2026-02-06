# Day 6: Signals and Noise

# Helper function; rearranges the messages by column/position
def rearrangeMessages(messages: list[str]):
    chars_by_position = []
    position_list = []

    for i in range(len(messages[0])):
        position_list.extend([msg[i] for msg in messages])
        chars_by_position.append("".join(position_list))
        position_list.clear()
    
    return chars_by_position

# Helper function which does the work of counting the frequency of each letter at each position
def generateFrequencyTable(chars_by_position: list[str]):
    # A separate frequency table and set for already found letters are kept for each position
    freq = [{} for _ in range(len(chars_by_position))]
    found = [set() for _ in range(len(chars_by_position))]

    for i, chars in enumerate(chars_by_position):
        for c in chars:
            if c not in found[i]:
                count = chars.count(c)
                freq[i][count] = c  # There should only be one character per position that is most/least frequent, so it is safe to only store the most recent character per count
                found[i].add(c)
    
    return freq


# Parts 1 and 2 (determined by the highest_frequency flag)
def decodeMessage(messages: list[str], highest_frequency: bool):
    freq_table = generateFrequencyTable(rearrangeMessages(messages))
    decoded_msg = []

    for freq_by_pos in freq_table:
        # Sorts the frequency table for this position and appends the character stored there; this represents the most/least common character for each column
        decoded_msg.append(freq_by_pos[sorted(freq_by_pos, reverse=highest_frequency)[0]])
    
    return "".join(decoded_msg)


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day06.txt", "r") as f:
            messages = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"If the most common character per position is to be used, {decodeMessage(messages, highest_frequency=True)} is the error-corrected version of the message.")  # Part 1
    print(f"If the least common character per position is to be used, {decodeMessage(messages, highest_frequency=False)} is the error-corrected version of the message.")  # Part 2