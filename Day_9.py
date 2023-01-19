# Dictionaries and lists

prog_dict = {
"Bug": "An error in a program",
"Function": "A piece of code that performs an action by taking an input and producing an output"
}

#  Create an empty dict
some_dict = {} 

# Access a dictionary element
prog_dict["Bug"]

# Add a new item to dict
prog_dict["Loop"] = "The action of repeating sth"

# Edit an item in a dict
prog_dict["Bug"] = "A twist of fate"

# Loop through a dict - Gives you the KEY from the dict
for key in prog_dict:
    print(key)

# To get the value from the dict:
for key in prog_dict:
    print(prog_dict[key])



# Create an empty list
some_list = []