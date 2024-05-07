# A program that calculates the sum of all the even numbers from 1 to X. 

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
if target > 1000:
  print("Please insert a number between 0 and 1000")

total = 0
for number in range(0, target+1):
  if number % 2 == 0:
    total += number

print(total)