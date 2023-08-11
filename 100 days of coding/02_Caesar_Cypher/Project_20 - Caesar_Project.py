# Caesar Cipher

from base64 import decode
import art

print (art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))




def caesar(direction, text, shift):
    tempList = []                                                                   # Create a list do transform the input text into a list of separated characters.
    finalList = []

    try:
        for letter in text:
            tempList.append(letter)
        
        for letter in tempList:

            if letter != " ":                                                           # If not a blank space, find the chosen letter in the alphabet list, using index;                                               
                position = alphabet.index(letter)
                                    
                if direction == "encode":                                               # Sum or not depending if it is decode or encode       
                    indexNumberFuture = position + shift                                
                elif direction == "decode":
                    indexNumberFuture = position - shift                                

                finalLetter = alphabet[indexNumberFuture]                        
                
                for letter in finalLetter :                                             # Add that new finalLetter in the finalList;
                    finalList.append(letter)
            else:                                                                       # Exception created for the black space
                finalList.append(letter)
            
        print (f'Your {direction}d code is {"".join(finalList)}')

    except  IndexError:
        shift = int(input("Type a valid number:\n"))
        if IndexError == False:
            pass
        else:
            shift = int(input("Type a valid number:\n"))


#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).




caesar (direction, text, shift)