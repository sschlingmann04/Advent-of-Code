# Day 5: How About a Nice Game of Chess?

from hashlib import md5

# Parts 1 and 2 (determined by the position_encoding flag)
def generatePassword(key: str, match: str, position_encoding = False):
    prefix = key.encode()
    num = 0
    # Create an empty list if positions within the password are not being encoded; otherwise pre-fill all 8 positions in the password with None
    password = [] if not position_encoding else [None] * 8

    while True:
        res = md5(prefix + str(num).encode()).hexdigest()

        # Part 1
        if not position_encoding:
            # If the hexadecimal representation of the hash starts with the match...
            if res.startswith(match):
                password.append(res[5])  # Append the 6th character in the hash to the password
                # If the password has 8 characters in it, then return the complete password
                if len(password) == 8:
                    return "".join(password)
        
        # Part 2
        else:
            if res.startswith(match):
                # res[5] is the 6th character of the password
                pos = res[5]
                # If the 6th character is a digit and it is within the range 0-7 and the corresponding position within the password has not been filled yet...
                if pos.isdigit() and 0 <= int(pos) < 8 and not password[int(pos)]:
                    password[int(pos)] = res[6]  # Add the 7th character in the hash to the position in the password referenced by the 6th character in the hash
                    # If all positions have been filled, then return the completed password
                    if None not in password:
                        return "".join(password)
        
        num += 1


# Example main program
if __name__ == "__main__":
    try:
        with open("2016/input_files/day05.txt", "r") as f:
            key = f.read().strip()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    print(f"The password is {generatePassword(key, "00000")} for the door with ID {key}.")  # Part 1
    print(f"Using a new position encoding method for extra security, {generatePassword(key, "00000", position_encoding=True)} is the new password.")  # Part 2