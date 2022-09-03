from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#def to check if the number is int, if not, keep on trying
def checkint (number):
    while True:
        try: 
            resp = int(input(number)) #The number that the user has to input is intenger, of not, it will give the bellow error.
        except ValueError:
            print("Invalid Number") #This one
            continue
        else:
            return resp
            break # In the case of there's no error, then its done.

print ("Welcome to the game!")

while True:
    usuario = checkint("Which one do you choose?\n1 - Rock\n2 - Paper\n3 - Scissors?\nYour answer: ")
    if usuario < 0 or usuario > 4:
        continue
    else:
        break

computer = randint(1, 3)

if computer == 1:
    computer = rock
elif computer == 2:
    computer = paper    
elif computer == 3:
    computer = scissors

if usuario == 1:
    usuario = rock
elif usuario == 2:
    usuario = paper
elif usuario == 3:
    usuario = scissors    

print (f"You choice {usuario}\nComputer's choice {computer}")


if computer == rock and usuario == rock or computer == paper and usuario == paper or computer == scissors or usuario == scissors:
    print ("It is a drawn!")
elif computer == rock and usuario == paper or usuario == rock and computer == paper:
    print ("Rock vs Paper = Paper Wins!")
elif computer == rock and usuario == scissors or computer == scissors and usuario == rock:
    print ("Rock vs Scissors = Rock Wins!")
elif computer == paper and usuario == scissors or computer == scissors and usuario == paper:
    print ("Paper vs Scissors = Scissors Wins!")

