# Guessing number game
# Create a game with two levels - easy: 10 guesses and hard: guesses
# Create a random number 
# ask the user to guess the random naumber
#  continue guessing until the user gets the answer 
import random

hidden_num = random.randint(0, 101)
print(hidden_num)

def game():
    guess_true = True
    guess = input("Guess the number from 0 to 100: ")
    guess_count = 4
    while guess_count < 4:
        if guess == hidden_num:
            print("You guessed it right!")
        else: 
            guess_count -= 1
            print("Sorry, not this time")
            game()

game()

