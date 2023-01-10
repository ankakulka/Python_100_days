# Get the input and save it in a variable
name = input('What is your name?')
# Print out the length of the captured string
print(len(name))

# Write a program that switches the values stored in the variables a and b.
a = input("a: ")
b = input("b: ")

a,b = b,a

print("a: " + a)
print("b: " + b)

