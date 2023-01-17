# Create a hangman game 

# Flow:
# 1.a. Create a variable holding a random word
# 1.b. Print the number of letters to the console as blanks
# 2: Ask for input - a single letter
# 3: Check if the provided letter is present in the random word
# If YES: 
#   IF the word has NOT been filled
#       Add the word to the blanks variable AND print the letter the user has given in the correct place
#       GO back to point 2
#   IF the word HAS been filled, print: YOU WIN

# IF NO: 
#   IF the the HANGMAN IS filled: print (You lose), end game
#   IF the HANGMAN is NOT filled
#       Add the body part to the hangman and go back to point 2. 


# SUB TASK 1

#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
#Randomly choose a word from the word_list and assign it to a variable called chosen_word
list_len = len(word_list)
random_pick = random.randint(0, list_len - 1)
chosen_word = word_list[random_pick]
# print(type(chosen_word))
# split the word into a list
hidden_word = chosen_word.split()
print(type(hidden_word))
# 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letter_from_user = input("Give me a single letter: ").lower()
# check at which position the letter_from_user occurs in the hidden_word

#3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# Iterate over the chosen word to check if letter_given occurs
LIFE_COUNTS = 9

display = []
for _ in chosen_word:
    display += "_"
print(display)


# for letter in chosen_word:
#     if letter == letter_from_user:
#         print("YES")
#         # Loop through the word and replace the _ with the letter_from_user
#         letter_index = chosen_word.index(letter_from_user)
#         hidden_word.insert(letter_index,letter_from_user)
#         print(letter_index)
#     else:
#         letter_index = chosen_word.index(letter_from_user)
#         blanks = hidden_word.insert(letter_index, "_")
#         print(blanks)
        # Lose one life from LIFE_COUNTS

        
for position in range(list_len):
    letter = chosen_word[position]
    if letter == letter_from_user:
        display[position] = letter
   
print(display)
