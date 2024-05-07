# a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

age = input()
current_age_int = int(age)
weeks_left = (90 - current_age_int) * 52

print(f"You have {weeks_left} weeks left.")