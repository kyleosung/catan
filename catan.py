
from time import sleep
from random import randint
from matplotlib import pyplot as plt


roll = lambda: randint(1,6) + randint(1,6)





class Game():

    def __init__(self):
        self.rolls = 0

        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0
        self.sevens = 0
        self.eights = 0
        self.nines = 0
        self.tens = 0
        self.elevens = 0
        self.twelves = 0
    
    def update_roll(self, x):
        self.rolls += 1

        if x == 2:
            self.twos += 1
        elif x == 3:
            self.threes += 1
        elif x == 4:
            self.fours += 1
        elif x == 5:
            self.fives += 1
        elif x == 6:
            self.sixes += 1
        elif x == 7:
            self.sevens += 1
        elif x == 8:
            self.eights += 1
        elif x == 9:
            self.nines += 1
        elif x == 10:
            self.tens += 1
        elif x == 11:
            self.elevens += 1
        elif x == 12:
            self.twelves += 1

    def export(self):
        return {2: self.twos, 3: self.threes, 4: self.fours, 5: self.fives, 6: self.sixes, 7: self.sevens, 8: self.eights, 9: self.nines, 10: self.tens, 11: self.elevens, 12: self.twelves}

def turn():
    return

def main():

    g = Game()

    # while True:
    #     choice = input("\nClick Enter to Roll the Dice! (or type q to end the game)")

    #     if choice == "q":
    #         break

    #     x = roll()

    #     print(f"On turn {g.rolls}, you rolled a {x}!")

    #     g.update_roll(x)

    while g.rolls < 1500:
        x = roll()

        print(f"On turn {g.rolls}, you rolled a {x}!")

        g.update_roll(x)



    
    roll_data = g.export()

    print("Here are the number for each die roll")

    for k, v in roll_data.items():
        print(f'{k}: {v}, or approximately {v / g.rolls}')

    rolls = list(roll_data.keys())
    values = list(roll_data.values())

    plt.bar(rolls, values, color ='maroon')
    plt.xlabel("Rolls")
    plt.ylabel("Number of Each Roll")
    plt.show()

    return


if __name__ == "__main__":
    main()