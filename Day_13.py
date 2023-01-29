# Debugging

# Decribe the problem 
#  Why is i not printing:

def my_func():
    for i in range(0, 20):
        if i == 20:
            print("You got it")


my_func()

#  range() gives us the 0-19, not including the second parameter. 
#  TO get 20 you would need to specify the range(0, 21)

# Similarly, in this case
from random import randint
dice_img = ["@", "$", "£", "%", "*", "#"]
dice_num = randint(0,5)
print(dice_img[dice_num])

# What about year 1994? < > are not inclusive.
#  So add = sign. I 
year = int(input("What's the year of your birth? "))
if year > 1980 and year < 1994:
    print("You're a millenial")
elif year >= 1994:
    print("You're a Gen-Z")


# Mutating a list
#  Use a pythontutor.com to debug



def mutate(a_l):
  b_l = []
  for item in a_l:
    new_item = item * 2
    # This line must be inside the loop 
    b_l.append(new_item)
  print(b_l)

mutate([1,2,3,5,8,13])