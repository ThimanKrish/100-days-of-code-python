# You are going to write a program that will mark a spot on a map with an X.

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

column = position[0]
raw = position[1]

column_position = 0
raw_position = 0
if column == 'A':
  column_position = 1
if column == 'B':
  column_position = 2
if column == 'C':
  column_position = 3

if raw == '1':
  raw_position = 1
if raw == '2':
  raw_position = 2
if raw == '3':
  raw_position = 3

map[raw_position-1][column_position-1] = 'X'


print(f"{line1}\n{line2}\n{line3}")