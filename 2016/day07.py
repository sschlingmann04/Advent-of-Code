# Day 7: Internet Protocol Version 7

# Part 1
def find_TLS_IPs(IPs: list[list[str]]):
    TLS_IPs = []

    for IP in IPs:
        ABBA_found_inside_brackets, ABBA_found_outside_brackets = False, False
        for index, seq in enumerate(IP):
            # Creates a sliding window that checks each string of 4 consecutive characters in the sequence
            for i in range(0, len(seq) - 3):
                current_seq = seq[i:i+4]
                # If the sequence is a palindrome (reads the same forwards and reversed) and the first and second characters are different, it is a valid ABBA sequence
                if "".join(reversed(current_seq)) == current_seq and current_seq[0] != current_seq[1]:
                    # Based on how IPs have been parsed, the sequences outside square brackets always have even indexes and the ones inside square brackets always have odd indexes
                    # With this in mind, check if index is even or odd to determine whether this sequence was found inside or outside brackets
                    if index % 2 == 0:
                        ABBA_found_outside_brackets = True
                    else:
                        ABBA_found_inside_brackets = True
                    break
            
            if ABBA_found_inside_brackets:
                break
        
        if ABBA_found_outside_brackets and not ABBA_found_inside_brackets:
            TLS_IPs.append(IP)
    
    return TLS_IPs

# Part 2
def find_SSL_IPs(IPs: list[list[str]]):
    SSL_IPs = []

    for IP in IPs:
        ABAs_or_BABs = [set() for _ in range(2)]
        SSL_valid = False
        for index, seq in enumerate(IP):
            # Creates a sliding window that checks each string of 3 consecutive characters in the sequence
            for i in range(0, len(seq) - 2):
                current_seq = seq[i:i+3]
                # If the sequence is a palindrome and the first and second characters are different, it is a valid ABA/BAB sequence
                if "".join(reversed(current_seq)) == current_seq and current_seq[0] != current_seq[1]:
                    # Even and odd indexes corresponding to outside/inside brackets rule from before still applies here
                    # Therefore, add current sequence to either the ABA set (index 0, for outside brackets) or the BAB set (index 1, for inside brackets)
                    ABAs_or_BABs[index % 2].add(current_seq)

                    # Check the other set for a corresponding ABA/BAB sequence
                    if (current_seq[1] + current_seq[0] + current_seq[1]) in ABAs_or_BABs[index % 2 - 1]:
                        SSL_valid = True
                        break
            
            if SSL_valid:
                break
        
        if SSL_valid:
            SSL_IPs.append(IP)
    
    return SSL_IPs


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day07.txt", "r") as f:
            IPs = [line.replace("[", "]").strip().split("]") for line in f.readlines()]
    except FileNotFoundError:
        print("Error: File was not found!")

    print(f"There are {len(find_TLS_IPs(IPs))} IPs that support transport-layer snooping (TLS).")  # Part 1
    print(f"There are {len(find_SSL_IPs(IPs))} IPs that support super-secret listening (SSL).")  # Part 2