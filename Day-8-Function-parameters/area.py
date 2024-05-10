# Write your code below this line 👇
import math

def paint_calc(height, width, cover):
  number_of_cans = (test_h * test_w) / coverage
  print(f"You'll need {int(math.ceil(number_of_cans))} cans of paint.")  

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)