# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

#     Take both people's names and check for the number of times the letters in the word TRUE occurs.

#     Then check for the number of times the letters in the word LOVE occurs.

#     Then combine these numbers to make a 2 digit number.




print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

both_names = name1 + name2
lower_name = both_names.lower()

name_to_array = list(lower_name)
t = name_to_array.count("t")
r = name_to_array.count("r")
u = name_to_array.count("u")
e = name_to_array.count("e")

l = name_to_array.count("l")
o = name_to_array.count("o")
v = name_to_array.count("v")

total_1 = t+r+u+e
total_2 = l+o+v+e

love_score = str(total_1) + str(total_2)
int_score = int(love_score)

if int_score < 10 or int_score > 90:
  print(f"Your score is {int_score}, you go together like coke and mentos.")
elif int_score < 50 and int_score > 40:
  print(f"Your score is {int_score}, you are alright together.")
else:
  print(f"Your score is {int_score}.")