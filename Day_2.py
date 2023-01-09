# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")

a = int(two_digit_number[0])
b = int(two_digit_number[1])
c = a + b
print(c)

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Convert str to float
w = float(weight)
h = float(height)
BMI = w/(h*h)

# Warning you should convert the result to a whole number: type conversion float to int to str
BMI_console = str((int(BMI)))
print(BMI_console)

# FStrings: Life in weeks, months and days
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age? ")

const_age = int(age)
const_death = 90
const_months = const_death * 12
const_weeks = const_death * 52
const_days = const_death * 365
x = str(const_days - const_age * 365)
y = str(const_weeks - const_age * 52)
z = str(const_months - const_age * 12 )

print(f"You have {x} days, {y} weeks, and {z} months left.")

# Tip Calculator

print("Welcome to the tip calculator")
bill_input = input("What was the total bill? ")
tip_input = input("What percentage tip would you like to give? 10, 12, or 15? ")
ppl_input = input("How many people to split the bill? ")

bill_total = float(bill_input)
tip = float(tip_input)
ppl_num = float(ppl_input)

tip_amount = bill_total * (tip /100) 
amount_to_pay = (bill_total + tip_amount) / ppl_num

# Round the result to the 2 decimal points and convert to str type
final_amount = str(round(amount_to_pay, 2))

# Print the result
print(f"Each person should pay ${final_amount}")