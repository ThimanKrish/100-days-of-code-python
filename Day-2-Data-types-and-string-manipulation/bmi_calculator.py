
# a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

bmi = int(weight) / (float(height) * float(height))

print(str(int(bmi)))