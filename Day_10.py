# Functions with outputs
# In Python it is possible to return multiple values from a function by separating them with a comma
# The canonical way to return multiple values in languages that support it is often tupling.

#  Task: create a function with two parameters

def name_conv(first, last):
    # first = input("What is your first name: ")
    # last = input("What is your last name? ")
    f_ed = first.title()
    l_ed = last.title()
    print(f"Welcome {f_ed} {l_ed}")
 
# Refactored leap year:
def is_leap(year):
    if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
        return True
    else:
        return False


# Calculator

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(num1,num2):
  return num1 / num2


# Create a dict where KEYS are the symbols use
#  VALUES are the result of the functions
operations = {
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
}

num1 = float(input("What's the first number? "))
num2 = float(input("What's the second number? "))
op_sym = input("Which operation would you like to perform? ")


# for i in operations:
#     if ask == i:
#         answer = operations[i]
#         print(f"{num1} {i} {num2} results in {answer}")

# This gives an unexpected result: 
# 2 + 3 results in <function add at 0x000001AEE14798A0>

# Task can be ssolved by passing the dictionary key to a function
calc_func = operations[op_sym]
answer = calc_func(num1, num2)

print(f"{num1} {op_sym} {num2} results in {answer}")


# Another approach to solve by using else if statements


# while True:
    # take input from the user
    # choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    # if choice in ('1', '2', '3', '4'):
    #     try:
    #         num1 = float(input("Enter first number: "))
    #         num2 = float(input("Enter second number: "))
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")
    #         continue

    #     if choice == '1':
    #         print(num1, "+", num2, "=", add(num1, num2))

    #     elif choice == '2':
    #         print(num1, "-", num2, "=", subtract(num1, num2))

    #     elif choice == '3':
    #         print(num1, "*", num2, "=", multiply(num1, num2))

    #     elif choice == '4':
    #         print(num1, "/", num2, "=", divide(num1, num2))
        
    #     # check if user wants another calculation
    #     # break the while loop if answer is no
    #     next_calculation = input("Let's do next calculation? (yes/no): ")
    #     if next_calculation == "no":
    #       break
    # else:
    #     print("Invalid Input")


# RECURSION 
# You can call a function within the def of the function
# 
def calculator():
    num1 = float(input("Gimme me a number: ")) 
    for i in operations:
        print(i)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Gimme me more: ")) 
        calc_func = operations[operation_symbol]
        answer = calc_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} result in {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a nwe calculation ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()



