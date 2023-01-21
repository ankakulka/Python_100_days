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
