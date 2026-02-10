# Day 9: Explosives in Cyberspace

# Helper function for handling markers
def handleMarker(txt: str, pos: int):
    # Find the first character after the end of the marker, represented by ")"
    current_pos = pos
    pos = txt.find(")", pos) + 1
    marker = txt[current_pos + 1:pos - 1]  # Slice to get the full marker string (excluding the parentheses)

    # Return the number of characters and number of times they should be repeated, along with the index of the character immediately following the marker
    num_chars, num_repeats = [int(x) for x in marker.split("x")]
    return num_chars, num_repeats, pos


# Part 1
def decompressText_v1(txt: str):
    decompressed_txt = []
    i = 0  # Manual index counter

    while i < len(txt):
        # The "normal" case: just add the character itself to the list
        if txt[i] != "(":
            decompressed_txt.append(txt[i])
            i += 1
        # If the next character is a "(", then it is the start of a marker
        else:
            num_chars, num_repeats, i = handleMarker(txt, i)

            # Take the next x amount of characters and repeat them y times according to the marker; add this string to the list
            current_pos = i
            i += num_chars
            decompressed_txt.append(txt[current_pos:i] * num_repeats)
    
    return len("".join(decompressed_txt))

# Part 2
def decompressText_v2(txt: str):
    length = 0
    i = 0  # Manual index counter

    while i < len(txt):
        # Base case: increment the length by 1 if it is not a marker
        if txt[i] != "(":
            length += 1
            i += 1
        # If the next character is a "(", then it is the start of a marker
        else:
            num_chars, num_repeats, i = handleMarker(txt, i)

            # Take the next amount of x characters, calculate the decompressed length of that entire string (marker multipliers included), and mutliply result by number of repeats
            current_pos = i
            i += num_chars
            length += decompressText_v2(txt[current_pos:i]) * num_repeats
    
    return length


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day09.txt", "r") as f:
            txt = f.read()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"The decompressed length of the file is {decompressText_v1(txt)} characters.")  # Part 1
    print(f"However, by using the improved version 2 format, the decompressed length of the file is {decompressText_v2(txt)} characters.")  # Part 2