# 🚨 Don't change the code below 👇
row1 = ["0","0","0"]
row2 = ["0","0","0"]
row3 = ["0","0","0"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆


horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")