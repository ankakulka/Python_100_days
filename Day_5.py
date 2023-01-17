# Loops
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#  Python comes in with a built-in sum() and round() functions
length = len(student_heights)
print(round(sum(student_heights) / length))

## print the numbers from 0 through 99
for i in range(100):
  print(i)

# While
i = 0
while i < (len(my_list)):
    v = my_list[i]
    print(v)
    i += 1

#  FOR LOOPS - PRint value
for i in range(len(my_list)):
    v = my_list[i]
    print(v)

for v in my_list:
    print(v)

# for name in iterable:
    # stataments    

# Lists => elements
for e in [1,2,3,4,5]:
    print(e)

#  Strings => characters

for c in "Hello":
    print(c)

# Also see ned batchelder Loop like a native