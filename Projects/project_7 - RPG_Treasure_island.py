print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input ("You're at a cross road. Where do you want to go?\nA - Continuing going forward\nB - Turn left\nC - Turn Right\nYour answer:  ").lower()
if choice1 == "a":
    print("You come to a lake. There is an island in the middle of the lake.\n")
    choice2 = input("Do you prefer to wait for a boat, or try to swin for it?\nA - Swim\nB - Wait\nYour answer:  ").lower()
    if choice2 == "b":
        print ("You arrive at the island unharmed.\n")
        choice3 = input("There is a house with 3 doors. One red, one yellow and one blue.\nWhich colour do you choose?\nA - Red\nB - Yellow\nC - Blue\nYour answer: ").lower()
        if choice3 == "a":
            print ("You've just got killed by a bear. Game Over.")
        elif choice3 == "b":
            print ("Motherload! You've found the treasure. Congrats!")
        elif choice3 == "c":
            print ("You'got burned by fire. Game Over")
        else:
            print("Game Over.")
    else:
        print ("The sharks ate you. Game Over")    
else:
    print ("You fell into a trap and died. Game Over")
    quit()
