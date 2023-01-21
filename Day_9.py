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

# Replace the VALUES from student_scores dict with values based on certain condition
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# Values (scores in this dict) in the dict student_scores to replace with:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

# 1. Create an empty dictionary called student_grades.
student_grades = {}

# 2. Loop throught the dict containing scores
for key in student_scores:
    # add a score variable and access the VALUE of the student scores
    score = student_scores[key] 
    if score > 90:
        student_grades[key] = "Outstanding"
    elif score > 80:
        student_grades[key] = "Exceeds Expectations"
    elif score > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


# Add dict to a list using a function
# append() func to add a dict to a list
# update() func to add values to a dict new.dict.update({"key":value})
travel_log = []
# 
def add_new_country(country, num_visits, cities):
    new_dict = {}
    travel_log.append(new_dict)
    new_dict.update({"country": country})
    new_dict.update({"visits": num_visits})
    new_dict.update({"cities": cities})

# Call a func
add_new_country("France", 4, ["Paris", "Marseille", "Nice", "Toulouse"])

print(travel_log)

#  Connections map: use a func to create a dict of connections
connections = []
def train_connections(origin, destinations, region):
    new_dict = {}
    connections.append(new_dict)
    new_dict.update({"origin": origin})
    new_dict.update({"destinations": destinations})
    new_dict.update({"region": region})


#  Resizing imgs with PIL lib
import PIL
low_res_img = img.resize((img.width // 4, img.height // 4))
low_res_img.show()



