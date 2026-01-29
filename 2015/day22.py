# Day 22: Wizard Simulator 20XX

from math import inf
from copy import deepcopy

# Character-related classes: "Character" is the base class, with "Player"/"Boss" as the derived classes
class Character:
    def __init__(self, name, hit_points):
        self.name = name
        self.HP = hit_points

class Player(Character):
    def __init__(self, name, hit_points, armor, mana):
        super().__init__(name, hit_points)
        self.DEF = armor
        self.mana = mana
        self.total_spent = 0

class Boss(Character):
    def __init__(self, name, hit_points, damage):
        super().__init__(name, hit_points)
        self.DMG = damage


# Spell-related classes: "Spell" is the base class and "Effect" is the derived class
class Spell:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Effect(Spell):
    def __init__(self, name, cost, timer = 0):
        super().__init__(name, cost)
        self.timer = timer


# Helper function for cleanly initializing all spells
def initializeSpells():
    return [Spell("Magic Missile", 53), Spell("Drain", 73), Effect("Shield", 113), Effect("Poison", 173), Effect("Recharge", 229)]

# Helper function for applying any active effects at the start of a turn
def applyEffects(player: Player, boss: Boss, active_effects: list[Effect]):
    player.DEF = 0

    for e in active_effects[:]:
        if e.name == "Shield":
            player.DEF = 7
        elif e.name == "Poison":
            boss.HP -= 3
        elif e.name == "Recharge":
            player.mana += 101
        else:
            raise ValueError("Unexpected effect!")
        
        # Decrease the timer by 1; if the timer hits 0 then the effect is no longer active and should be removed
        e.timer -= 1
        if e.timer == 0:
            active_effects.remove(e)


# Parts 1 and 2 (determined by the hard_mode_enabled variable)
def minimizeManaForVictory(hard_mode_enabled):
    # While this is the function that is called, the real magic happens in the next function
    for s in spells:
        simulateTurn(Player("Player", 50, 0, 500), deepcopy(boss), s, [], [], hard_mode_enabled)

# Actual function that does the heavy lifting in simulating turns given a spell to use and the current battle state
def simulateTurn(player: Player, boss: Boss, turn_spell: Spell, current_seq: list[str], active_effects: list[Effect], hard_mode_enabled):
    global min_cost_victory

    # Before even starting, if the total amount the player has spent is more than the current minimum cost, then there is no need to continue further
    if player.total_spent >= min_cost_victory[0]:
        return False

    # Player's turn first
    # If hard mode is enabled the player will lose 1 HP at the start of their turn; if the player dies as a result of this they lose
    if hard_mode_enabled:
        player.HP -= 1
        if player.HP == 0:
            return False
    
    # If there are any effects to handle, do them now before the turn starts
    applyEffects(player, boss, active_effects)
    
    # If the boss was killed by the poison effect the turn instantly ends and the player wins
    if boss.HP <= 0:
        if player.total_spent < min_cost_victory[0]:
            min_cost_victory = (player.total_spent, current_seq)  # The player's spell for this turn was never used so only the current sequence of spells is needed
        return True

    # Before casting the player's spell they have to first pay its cost in mana
    player.mana -= turn_spell.cost
    # If our mana goes into the negatives (they could not afford it) or if an effect caused by this spell is already active, then the spell cannot be used and the player has lost
    if player.mana < 0 or any(e.name == turn_spell.name for e in active_effects):
        return False
    
    # Otherwise, the spell can be used, and in turn the player's total mana spent will increase
    player.total_spent += turn_spell.cost
    current_seq.append(turn_spell.name)  # Add the player's spell for this turn to the current sequence of spells used

    # Handle each spell
    if turn_spell.name == "Magic Missile":  # Magic Missile instantly deals 4 damage to the boss
        boss.HP -= 4
    elif turn_spell.name == "Drain":  # Drain instantly deals 2 damage to the boss and restores 2 HP to the player
        boss.HP -= 2
        player.HP += 2
    elif turn_spell.name == "Shield":  # Shield sets the player's defense/armor to 7 for as long as it is active (6 turns)
        active_effects.append(Effect("Shield", 113, 6))
        player.DEF = 7
    elif turn_spell.name == "Poison":  # Poison deals 3 damage to the boss at the start of every turn for as long as it is active (6 turns)
        active_effects.append(Effect("Poison", 173, 6))
    elif turn_spell.name == "Recharge":  # Recharge awards 101 mana to the player at the start of every turn for as long as it is active (5 turns)
        active_effects.append(Effect("Recharge", 229, 5))
    else:
        raise ValueError("Unexpected spell!")
    
    # If the boss was killed then the player wins
    if boss.HP <= 0:
        if player.total_spent < min_cost_victory[0]:
            min_cost_victory = (player.total_spent, current_seq)
        return True
    
    # Now it's the boss' turn
    # Once again handle any effects before the turn starts
    applyEffects(player, boss, active_effects)
    
    # If the boss was killed by the poison effect the turn instantly ends and the player wins
    if boss.HP <= 0:
        if player.total_spent < min_cost_victory[0]:
            min_cost_victory = (player.total_spent, current_seq)
        return True

    # If the boss is still alive by this point they will now have a chance to attack the player
    player.HP -= max(boss.DMG - player.DEF, 1)

    # If the player was killed then the player lost (obviously)
    if player.HP <= 0:
        return False

    # If neither the player nor boss has been killed then another set of turns must be performed with each of the possible spells (effectively a depth-first search)
    for s in spells:
        # Deep copy everything except the current sequence to preserve the game state (deep copy is unnecessary since only appending is done on it)
        simulateTurn(deepcopy(player), deepcopy(boss), s, current_seq.copy(), deepcopy(active_effects), hard_mode_enabled)


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day22.txt", "r") as f:
            HP = int(f.readline().split(": ")[1])
            DMG = int(f.readline().split(": ")[1])
            boss = Boss("Boss", HP, DMG)
    except FileNotFoundError:
        print("Error: File was not found!")
    
    spells = initializeSpells()
    min_cost_victory = (inf, [])

    minimizeManaForVictory(hard_mode_enabled=False)
    print(f"On normal mode, the player can spend as little as {min_cost_victory[0]} mana and still win the fight.")  # Part 1

    min_cost_victory = (inf, [])
    minimizeManaForVictory(hard_mode_enabled=True)
    print(f"On hard mode, the player can spend as little as {min_cost_victory[0]} mana and still win the fight.")  # Part 2