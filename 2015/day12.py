# Day 12: JSAbacusFramework.io

import json

# Part 1
def sumAllNumbers(value):
    global total
    total += int(value)
    return int(value)

# Part 2
def ignoreRedObjects(dct):
    if "red" in dct.values():
        return None
    return dct


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day12.txt", "r") as f:
            doc = f.read()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    total = 0
    json.loads(doc, parse_int=sumAllNumbers)
    print(f"The sum of all numbers in the document is {total}.")  # Part 1

    total = 0
    doc = json.dumps(json.loads(doc, object_hook=ignoreRedObjects))
    json.loads(doc, parse_int=sumAllNumbers)
    print(f'Ignoring objects that have the value "red", the sum of all numbers in the document is {total}.')