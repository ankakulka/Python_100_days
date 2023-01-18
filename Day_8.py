#Write your code below this line 👇
import math
# Define a function called paint_calc() so that the code below works. 
def paint_calc(height,width,cover):
   num_roh = (height*width)/cover
   num_can = math.ceil(num_roh)
   print(f"You'll need {num_can} cans of paint.")

# Note: I used math module simplify rounding up by using the math.ceil() function
# You can also achieve the same result with round but the math.ceil() is simpler

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

