# Day 14: Reindeer Olympics

# Reindeer class
class Reindeer:
    def __init__(self, name, speed, flying_time, resting_time, points=0):
        self.name = name
        self.speed = speed
        self.flying_time = flying_time
        self.resting_time = resting_time
        self.points = points
    
    def calculateDistance(self, time):
        total_period_time = self.flying_time + self.resting_time
        distance_per_period = self.speed * self.flying_time
        num_periods = time // total_period_time
        leftover_time = time % total_period_time
        leftover_distance = min(self.speed * leftover_time, distance_per_period)
        return num_periods * distance_per_period + leftover_distance


# Part 1
def winning_reindeer_by_distance(deer: list[Reindeer], time: int):
    winning_reindeer = []  # Needs to be a list to handle tie cases for part 2
    max_distance = 0

    for d in deer:
        distance = d.calculateDistance(time)
        if distance > max_distance:
            max_distance = distance
            winning_reindeer.clear()
            winning_reindeer.append(d)
        elif distance == max_distance:  # Needed to handle tie cases for part 2
            winning_reindeer.append(d)
    
    return winning_reindeer, max_distance

# Part 2
def winning_reindeer_by_points(deer: list[Reindeer], time: int):
    for s in range(1, time + 1):
        winning_reindeer, distance = winning_reindeer_by_distance(deer, s)  # Distance variable is not needed here but must be thrown into a variable somewhere
        for w in winning_reindeer:
            w.points += 1
    
    winner = None
    max_points = 0

    for d in deer:
        if d.points > max_points:
            max_points = d.points
            winner = d
    
    return winner


# Example main program
if __name__ == "__main__":
    try:
        with open("2015/input_files/day14.txt", "r") as f:
            line = f.readline()
            deer = []
            while line:
                split_line = line.split()
                # Based on the format of each line, the name will always be at index 0, the speed at index 3, the flying time at index 6, and the resting time at index 13
                name, speed, flying_time, resting_time = split_line[0], int(split_line[3]), int(split_line[6]), int(split_line[13])
                deer.append(Reindeer(name, speed, flying_time, resting_time))
                line = f.readline()
    except FileNotFoundError:
        print("Error: File was not found!")
    
    time = 2503
    winner, distance = winning_reindeer_by_distance(deer, time)
    print(f"After {time} seconds, {winner[0].name} is the winner and has travelled {distance} km.")  # Part 1

    winner = winning_reindeer_by_points(deer, time)
    print(f"Using a points system, {winner.name} is the winner with {winner.points} points.")  # Part 2