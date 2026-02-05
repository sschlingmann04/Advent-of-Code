# Day 4: Security Through Obscurity

# Room class
class Room:
    def __init__(self, name, ID, checksum):
        self.name = name
        self.ID = ID
        self.checksum = checksum


# Helper function for getting the frequency of all letters in a room's name
def getFrequencyOfLetters(name: str):
    freq = {}
    found = set()

    for char in name:
        # Ignore if character is a hyphen or if it's been seen already (and thus its frequency has already been calculated)
        if char != "-" and char not in found:
            count = name.count(char)

            if freq.get(count):
                freq[count].append(char)
            else:
                freq[count] = [char]
            
            found.add(char)
    
    return freq


# Part 1
def getRealRooms(rooms: list[Room]):
    real_rooms, real_IDs = [], []

    for room in rooms:
        # Get the frequency of every single letter in the room's encrypted name
        freq_dict = getFrequencyOfLetters(room.name)

        # Build a list that is each letter sorted by their frequency
        most_common_letters = []
        for count in sorted(freq_dict, reverse=True):
            most_common_letters.extend(sorted(freq_dict[count]))  # If multiple letters have the same frequency, those letters should then be sorted alphabetically
        
        # The checksum must be the five most frequent letters (ties broken alphabetically); thus the resulting sequence of letters must start with the checksum
        if "".join(most_common_letters).startswith(room.checksum):
            real_rooms.append(room)
            real_IDs.append(room.ID)
    
    return real_rooms, real_IDs

# Part 2
def decryptRooms(rooms: list[Room]):
    for room in rooms:
        cipher = room.ID % 26
        decrypted_name = []

        for char in room.name:            
            if char == "-":  # Hyphens become spaces regardless of the shift cipher
                decrypted_name.append(" ")           
            else:  # Otherwise, shift the character by the cipher value; if its Unicode value goes beyond "z" then subtract 26 to bring it back within the a-z range
                decrypted_name.append(chr(ord(char) + cipher) if ord(char) + cipher <= ord("z") else chr(ord(char) + cipher - 26))
        
        # Join all characters together to create a new string: this is the decrypted name of the room
        room.name = "".join(decrypted_name)
    
    return rooms


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day04.txt", "r") as f:
            line = f.readline()
            rooms = []
            while line:
                name, rest = line.rsplit("-", 1)
                ID, checksum = rest.split("[")
                ID = int(ID)
                checksum = checksum.strip("]\n")

                rooms.append(Room(name, ID, checksum))
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    real_rooms, real_IDs = getRealRooms(rooms)
    print(f"The sum of the sector IDs is {sum(real_IDs)} for only the real rooms.")  # Part 1

    decrypted_rooms = decryptRooms(real_rooms)
    for room in decrypted_rooms:
        if "pole" in room.name:
            print(f"North Pole objects are stored in the aptly-named room \"{room.name}\", and {room.ID} is its sector ID.")  # Part 2
            break