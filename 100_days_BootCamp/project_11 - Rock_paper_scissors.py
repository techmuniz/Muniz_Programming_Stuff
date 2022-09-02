# Comparar quem ganhou ou perdeu
# Fazer o computador gerar uma resposta aleatória para ele

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

'''def numbervalidation (number):
    while True:
        try:
            answer = int(input(number))
        except ValueError:
            print("You need to choose a valid number!")
            continue
        else:
            print (answer)
            break'''




print ("welcome to the worlds most famous 'Hand' game!")


while True:
    try:
        choice =  int(input("Please, choose a number that you would like to play:\n1 - Rock\n2 - Paper\n3 - Scissors\nYour answer: "))
    except ValueError:
        print("You need to choose a valid number!")
        continue
    else:
        print (choice)
        break