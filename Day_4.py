# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random

flip = random.randint(0,1)
if flip == 0:
    print("Heads")
else:
    print("Tails")


# Banker roulette
#  Write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

list_len = len(names)

r_num = random.randint(0, list_len - 1)
payer = names[r_num]
print(f"{payer} is going to buy the meal today!")
