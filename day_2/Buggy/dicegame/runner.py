from .die import Die
# BUGS
# The counter resets from start each time - FIXED
# The numbers on the dice does not add up - FIXED
# Y/n in the end does not work - FIXED
# Check the last bit with the weird function - FIXED. utils.py not needed anymore.
# Removed unecessary def in die.py: - FIXED
        # def roll(dice):
        #    for die in dice:
        #        # XXX: I don't even know what this function does
        #        continue

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5) 
        self.reset() 
        
    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0
        self.consecutivewins = 0 # NEW Added to keep track of consecutive wins

    def reroll_dice(self): # NEW Added to roll new dice every round
        self.dice = Die.create_dice(5)  
        
    def answer(self): # CHANGED to count the eyes on the dice instead of the number of dice
        total = 0
        eye = 0
        for die in self.dice:
            eye = die.value 
            total = eye + total
        return total
        
    @classmethod
    def run(cls):
        runner = cls() # MOVED Creates an initial set of dice, with counter reset 
        while True:
            runner.reroll_dice()  # NEW Roll new dice each round without reseting counter
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                runner.consecutivewins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                runner.consecutivewins = 0
    
            print("Wins: {} Losses: {} Consecutive wins: {}".format(runner.wins, runner.loses, runner.consecutivewins))
            runner.round += 1

            if runner.consecutivewins == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                runner = cls() # NEW Rolls a new set of dice with counters reset in case the player wants to play again 

            prompt = input("Would you like to play again?[y/n]: ")

            if prompt == 'y' or prompt == '': 
                continue
            else:
                break # CHANGED Removed unecessary end function
