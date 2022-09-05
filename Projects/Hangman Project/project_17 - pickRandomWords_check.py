

import random

# 1º - Generate a list of words
word_list = ["aardvark", "baboon", "camel"]

# 2º - Choose a random word from that list 
chosen_word = random.choice(word_list)

# 3º - Create an empty list where we will later input the number of blanks and replace by the correct letters
display = []

# 4º - Create var to use as the user input answer
guess = str(input("Guess a letter: ")).lower()

# 5º - For each letter on the randomized chosen word, a "blank" is created inside the previous empty list
for letter in chosen_word:
    display.append("_")

# 6º - For each blank in the list, it is replaced by the letter in its due place inside the list. Important to remember the [x] after chosen_word, Display and insert.
for x in range(len(display)):
    if guess == chosen_word[x]:
        del display[x]
        display.insert(x, guess)

# 7º - Prints the list
print (display)


