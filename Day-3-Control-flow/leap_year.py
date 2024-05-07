# Write a program that works out whether if a given year is a leap year. 

# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    if (year % 100) % 2 == 0:
      print("Leap year")
    else:
      print("Not leap year")
else:
  print("Not leap year")