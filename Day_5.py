# Loops


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#  Python comes in with a built-in sum() and round() functions
length = len(student_heights)
print(round(sum(student_heights) / length))


