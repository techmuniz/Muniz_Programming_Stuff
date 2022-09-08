

import random
from turtle import clear
import hangman_words
import hangman_arts


# 1º - Generate a list of words and total number of lives
lives = int(6)

# 2º - Choose a random word from that list, create an empty list and then insert a "blank" representing each of the letters.
chosen_word = random.choice(hangman_words.word_list)
display = []
for letter in chosen_word:
    display.append("_")

# 3º - Print the "blanks" accordinly to the random.choice and let the game begins.
print (hangman_arts.logo)
print (display)
print (chosen_word)


while "_" in display:
    guess = str(input("Guess a letter: ")).lower()

    # 5º - In case user input a letter that already have...
    if guess in display:
      print (f"You've already sent that letter")

    # 6º - if input is incorrect you lose a life. It is important that this stays OUTSIDE the for loop.
    if guess not in chosen_word:
        lives -=1
        print(f"That letter '{guess}' is not in the list.")
        if lives == 0:
            print ("You lose")
            print (hangman_arts.stages[0])
            exit()

    # 7º - If the letter is correct, then use the loop to search where it is located and substitute de "blanks"
    for x in range(len(display)):
        if guess == chosen_word[x]:
            del display[x]
            display.insert(x, guess)
            if "_" not in display:
                print ("You won!")
                exit()

    # 4º - Use the "lives" to print the correct stage of the hangman
    print (hangman_arts.stages[lives])

    print(display)  




