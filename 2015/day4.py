# Day 4: The Ideal Stocking Stuffer

from hashlib import md5

# Parts 1 and 2 (determined by the match variable)
def findSecretNumber(key: str, match: str):
    num = 1
    while True:
        res = md5((key + str(num)).encode())
        if res.hexdigest().startswith(match):
            return num
        num += 1


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day4.txt", "r") as f:
            key = f.read()
    except FileNotFoundError:
        print(f"Error: File was not found!")
    
    print(f"The lowest positive number that produces a hash that starts with 5 zeroes is {findSecretNumber(key, "00000")}.")
    print(f"The lowest positive number that produces a hash that starts with 6 zeroes is {findSecretNumber(key, "000000")}.")