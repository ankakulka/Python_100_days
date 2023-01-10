# Conditional flow

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height < 120:
  print("Sorry you cannot go")
else:
  print("You can go")

#  Check if the number is even or odd

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Advanced BMI calculator

# My solution

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

w = float(weight)
h = float(height)
BMI = round(w/(h*h))

BMI_console = str((int(BMI)))

if BMI < 18.5:
    print(f"Your BMI is {BMI_console}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI_console}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI_console}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI_console}, you are obese.")
else:
    print(f"Your BMI is {BMI_console}, you are clinically obese.")

# You can also structure it slightly differently:

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")



year = float(input("Gimme a year: "))

# To check if it's a whole number:

year_mod = year.is_integer()

# Check if the year is not a leap year - is it a whole number when divided by 4?

if (year/4).is_integer() == False:
    print("Not a leap year")
elif (year/400).is_integer() == True:
    print("Also a LEAP")
elif (year/100).is_integer() == True:
    print("Surpisingly NOT a leap")
else:
    print("A leap year")