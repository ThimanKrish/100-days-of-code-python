# a program that calculates the average student height from a List of heights.

# Input a Python list of student heights
student_heights = input().split()
total_height = 0
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
  total_height += student_heights[n] 
  count += 1

avg_height = total_height / count
print(f"total height = {total_height}")
print(f"number of students = {count}")
print(f"average height = {round(avg_height)}")