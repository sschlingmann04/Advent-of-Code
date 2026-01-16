# Day 11: Corporate Policy

# This class utilizes operator overloading to make the rest of the code look cleaner. Thus, "password += 1" on line 29 can be interpreted as incrementing the string.
class Password:
    def __init__(self, password):
        self.password = password
    
    def __iadd__(self, inc):
        # inc will never be anything other than 1 in practice, but since a value is needed this loop is here to control how many times the string is incremented
        for i in range(inc):
            for j in range(len(self.password) - 1, 0, -1):  # j moves the index backwards starting from the end of the string
                self.password = self.password[:j] + chr(ord(self.password[j]) + 1) + self.password[j+1:]  # chr() and ord() converts from string to integer and vice versa

                # If the character we just incremented was "z", the next character in line in the ASCII table would be "{". If this happens, it should be replaced with "a"
                if self.password[j] == "{":
                    self.password = self.password.replace("{", "a")  # Must loop again to increment the character that came before it
                else:
                    break
        
        return self

    def __str__(self):
        return self.password


# Parts 1 and 2 (only the input changes between parts)
def findNextPassword(password: Password):
    while True:
        password += 1  # Start by incrementing the password
        pw = str(password)
        iol_condition = True

        # Condition 1: if password contains "i", "o", or "l", it is invalid and we must increment again
        for i in range(len(pw)):
            # Once we find the first character that is an "i", "o", or "l", we can "jump ahead" by setting all characters after said character to "z"
            if pw[i] == "i" or pw[i] == "o" or pw[i] == "l":
                iol_condition = False
                password = Password(pw[:i+1] + ("z" * (len(pw) - i - 1)))  # Now on the next increment the banned letter will no longer appear in the password
                break
        
        if not iol_condition:
            continue
        
        consec_condition, pairs_condition = False, False  # Conditions 2 and 3, respectively
        pairs_found = set()
        
        # Conditions 2 and 3 are checked within this loop
        for i in range(len(pw) - 1):
            # Condition 2: if password does not contain a straight sequence of at least 3 consecutive letters (abc, bcd, cde...), it is invalid and we must increment again
            if not consec_condition and i != len(pw) - 2 and ord(pw[i+1]) == ord(pw[i]) + 1 and ord(pw[i+2]) == ord(pw[i]) + 2:
                consec_condition = True
            # Condition 3: if password does not contain at least two different, non-overlapping pairs of letters (aa, bb, cc...), it is invalid and we must increment again
            if not pairs_condition and pw[i] == pw[i+1]:
                pairs_found.add(pw[i])  # Since this is a set, if a duplicate pair is found nothing will happen
                # If we found two different pairs then the condition has been met
                if len(pairs_found) == 2:
                    pairs_condition = True
            # If both conditions have been met (along with condition 1 above), the password is valid!
            if consec_condition and pairs_condition:
                return pw
        
        # If we made it here then at least one condition was not satisfied and the loop will reset as a result


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day11.txt", "r") as f:
            password = Password(f.read())  # Creating a Password object
    except FileNotFoundError:
        print("Error: File was not found!")

    # Part 1    
    new_password = findNextPassword(password)
    print(f"Santa's next password should be {new_password}.")

    # Part 2
    password = Password(new_password)
    newer_password = findNextPassword(password)
    print(f"After that, Santa's next password should be {newer_password}.")