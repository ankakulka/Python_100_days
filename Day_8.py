#Write your code below this line 👇
import math
# Define a function called paint_calc() so that the code below works. 
def paint_calc(height,width,cover):
   num_roh = (height*width)/cover
   num_can = math.ceil(num_roh)
   print(f"You'll need {num_can} cans of paint.")

# Note: I used math module simplify rounding up by using the math.ceil() function
# You can also achieve the same result with round but the math.ceil() is simpler:
# math.ceil(x)
# Return the ceiling of x, the smallest integer greater than or equal to x. 
# If x is not a float, delegates to x.__ceil__, 
# which should return an Integral value.

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


# Positional arguments : the position of the argument matters
paint_calc("6", "7", "cover")
# Keyword arguments: you can switch the order 
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime numbers
# Prime number are those that can be divided only by itself and 1 to get an integer

#  Pseudo-code
#  Range of numbers from 0-100 
#  some_num  int input (Give me a number: )
#  Iterate over the range - if not divisible by other numbers than one and self
#  then it is prime

#  In the range of divisio if True occurs more than two times - NOT prime
#  otherwise prim

#Write your code below this line 👇
basic_range = range(1,101)

def prime_checker(number):
    prime_list = []
    for i in basic_range:
        division = (number/i)
        if division.is_integer() == True:
            prime_list.append(division)
            print(len(prime_list))
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# Another - simpler? approach, using modulo:

#Write your code below this line 👇
basic_range = range(1,101)

def prime_checker(number):
    prime_list = []
    for i in basic_range:
        div_num = (number % i)
        prime_list.append(div_num)
    # Check if 0 occurs in prime_list more than 2 times -
    # then NOT prime


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
