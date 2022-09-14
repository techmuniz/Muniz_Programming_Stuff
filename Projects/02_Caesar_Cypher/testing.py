# Caesar Cipher

from base64 import decode


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(direction, text, shift):
    tempList = []                                                                   # Create a list do transform the input text into a list of separated characters.
    for letter in text:
        tempList.append(letter)
    
    finalList = []
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
        
    print (finalList)

