# Day 21: RPG Simulator 20XX

from itertools import product
from math import ceil

# Classes to store various attributes of various objects
class Character:
    def __init__(self, hit_points, damage, armor):
        self.HP = hit_points
        self.DMG = damage
        self.DEF = armor

class Gear:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# The following three classes are all derived from the base "Gear" class
class Weapon(Gear):
    def __init__(self, name, cost, damage):
        super().__init__(name, cost)
        self.DMG = damage

class Armor(Gear):
    def __init__(self, name, cost, armor):
        super().__init__(name, cost)
        self.DEF = armor

class Ring(Gear):
    def __init__(self, name, cost, damage, armor):
        super().__init__(name, cost)
        self.DMG = damage
        self.DEF = armor


# Helper functions. First is one to setup the shop and assign all values properly
def setupShop():
    weapons, armor, rings = [], [], []

    # No "None" added to weapons since buying a weapon is required
    weapons.append(Weapon("Dagger", 8, 4))
    weapons.append(Weapon("Shortsword", 10, 5))
    weapons.append(Weapon("Warhammer", 25, 6))
    weapons.append(Weapon("Longsword", 40, 7))
    weapons.append(Weapon("Greataxe", 74, 8))

    # "None" added to armor since buying armor is optional
    armor.append(None)
    armor.append(Armor("Leather", 13, 1))
    armor.append(Armor("Chainmail", 31, 2))
    armor.append(Armor("Splintmail", 53, 3))
    armor.append(Armor("Bandedmail", 75, 4))
    armor.append(Armor("Platemail", 102, 5))

    # "None" added to rings since buying rings are optional
    rings.append(None)
    rings.append(Ring("Damage +1", 25, 1, 0))
    rings.append(Ring("Damage +2", 50, 2, 0))
    rings.append(Ring("Damage +3", 100, 3, 0))
    rings.append(Ring("Defense +1", 20, 0, 1))
    rings.append(Ring("Defense +2", 40, 0, 2))
    rings.append(Ring("Defense +3", 80, 0, 3))

    return weapons, armor, rings

# Generates all possible combinations of weapons/armor/rings
def generateCombinations(weapons: list, armor: list, rings: list):
    result = list(product(weapons, armor, rings, rings))  # Rings listed twice since up to 2 rings can be bought
    gold_combos = {}

    for i in result:
        wpn, arm, rng1, rng2 = i[0], i[1], i[2], i[3]
        # Checks to make sure both rings generated are distinct to one another (unless they are both "None", i.e. no rings were bought)
        if rng1 != rng2 or (rng1 is None and rng2 is None):
            # A weapon is always required and so a cost is always guaranteed; for the others however the generated armor/ring(s) can be None so 0 should be used instead
            total_cost = wpn.cost
            total_cost += arm.cost if arm is not None else 0
            total_cost += rng1.cost if rng1 is not None else 0
            total_cost += rng2.cost if rng2 is not None else 0

            if gold_combos.get(total_cost) is not None:
                gold_combos[total_cost].append(i)
            else:
                gold_combos[total_cost] = [i]
    
    return gold_combos

# Simulates the battle between the player and the boss and determines a winner
def simulateBattle(player: Character, boss: Character):
    # A character's net attack is always their damage subtracted by their opponent's defense/armor, should this difference be a non-natural number the net attack defaults to 1
    net_player_attack = max(player.DMG - boss.DEF, 1)
    net_boss_attack = max(boss.DMG - player.DEF, 1)
    # The number of turns to guarantee a win for either character is always their opponent's HP divided by their own net attack calculated earlier (ceil ensures HP <= 0)
    turns_to_win = ceil(boss.HP / net_player_attack)
    turns_to_loss = ceil(player.HP / net_boss_attack)

    # If the player can win in fewer turns than they are guaranteed to lose by then the player wins! Otherwise, they lose... :(
    return turns_to_loss - turns_to_win >= 0


# Part 1
def minimizeGoldForVictory(gold_combos: dict):
    # Sorts all keys in the dictionary in order to examine the lowest total costs first
    sorted_costs = sorted(gold_combos.keys())

    for cost in sorted_costs:
        for i in gold_combos[cost]:
            wpn, arm, rng1, rng2 = i[0], i[1], i[2], i[3]
            # Once again a weapon is always required and so damage is always guaranteed; for the others 0 should be used for the appropriate stat when None is selected
            DMG = wpn.DMG
            DMG += rng1.DMG if rng1 is not None else 0
            DMG += rng2.DMG if rng2 is not None else 0

            DEF = arm.DEF if arm is not None else 0
            DEF += rng1.DEF if rng1 is not None else 0
            DEF += rng2.DEF if rng2 is not None else 0

            # Assign final stats to the player (base HP = 100); if the player can win with these stats then we have found the minimum cost needed for victory
            player = Character(100, DMG, DEF)
            if simulateBattle(player, boss) == True:
                return cost

# Part 2
def maximizeGoldForFailure(gold_combos: dict):
    # Sorts all keys in the dictionary, but now the list should be traversed in reverse to examine the highest total costs first
    sorted_costs = sorted(gold_combos.keys())

    for cost in reversed(sorted_costs):
        for i in gold_combos[cost]:
            wpn, arm, rng1, rng2 = i[0], i[1], i[2], i[3]
            # Once again a weapon is always required and so damage is always guaranteed; for the others 0 should be used for the appropriate stat when None is selected
            DMG = wpn.DMG
            DMG += rng1.DMG if rng1 is not None else 0
            DMG += rng2.DMG if rng2 is not None else 0

            DEF = arm.DEF if arm is not None else 0
            DEF += rng1.DEF if rng1 is not None else 0
            DEF += rng2.DEF if rng2 is not None else 0

            # Assign final stats to the player (base HP = 100); if the player can LOSE with these stats then we have found the maximum cost needed for failure
            player = Character(100, DMG, DEF)
            if simulateBattle(player, boss) == False:
                return cost


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day21.txt", "r") as f:
            HP = int(f.readline().split(": ")[1])
            DMG = int(f.readline().split(": ")[1])
            DEF = int(f.readline().split(": ")[1])
            boss = Character(HP, DMG, DEF)
    except FileNotFoundError:
        print("Error: File was not found!")
    
    gold_combos = generateCombinations(*setupShop())
    print(f"The player can spend as little as {minimizeGoldForVictory(gold_combos)} gold and still win the fight.")  # Part 1
    print(f"Conversely, the player can spend as much as {maximizeGoldForFailure(gold_combos)} gold and still lose the fight.")  # Part 2