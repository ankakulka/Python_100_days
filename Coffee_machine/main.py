# Py Charm
#
# - spell checker
# - style guide PEP 8
# - linter
# - refactoring
# - split screen
# - history
# - Structure

# Coffee machine project

from menu import MENU
from resources import resources

# print(MENU)
# Actions:
# Ask for the type of drink required
ask = input("Press the button to order espresso/latte/cappuccino: ")
# Ask for the amount of money needed - get the value of cost from the MENu dict
# print(ask)
tip = "Your drink is on the way. Please wait"
if ask == "espresso":
    print(f"Put {MENU['espresso']['cost']}$ into the coin slot")
    print(tip)
elif ask == "latte":
    print(f"Put {MENU['latte']['cost']}$ into the coin slot")
    print(tip)
else:
    print(f"Put {MENU['cappuccino']['cost']}$ into the coin slot")
    print(tip)


# Check if there are accessible resources
# Deduct the amount of coffee/sugar/milk from resources

# print report of resources available




