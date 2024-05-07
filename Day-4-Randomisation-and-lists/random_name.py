
# a program that will select a random name from a list of names.

names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.

import random

no_of_persons = len(names)

random_no = random.randint(0, no_of_persons - 1)
random_person = names[random_no]

print(f"{random_person} is going to buy the meal today!")