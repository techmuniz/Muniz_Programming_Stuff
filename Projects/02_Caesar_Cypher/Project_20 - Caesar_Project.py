

# Caesar Cipher

from base64 import decode


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (text, shift):
    tempList = []                                                              # Create a list do transform the input text into a list of separeted characters.
    for letter in text:
        tempList.append(letter)
    
    encodedList = []                                                            # Create the list that is going to be used the encripted code
    for letter in tempList:
        if letter is not " ":                                                   # If not a blank space, find the chosen letter in the alphabet list, using index;
            position = alphabet.index(letter)                                   
            indexNumberFuture = position + shift                                # Create the index that it will become by sum up with the "shift";
            encriptedLetter= alphabet[indexNumberFuture]                        
            for letter in encriptedLetter:                                      # Add that new encriptedLetter in the encodedList;
                encodedList.append(letter)
        else:                                                                   # Exception created for the black space
            encodedList.append(letter)
    
    encodedWords = "".join(encodedList)                                         # Transform the list into a string

    print (encodedWords)                                                        # The result is a encoded phrase
def decrypt (text, shift):                                                              
    tempList1 = []                                                              # Create a list do transform the input text into a list of separeted characters.   
    for letter in text:
        tempList1.append(letter)
    #print(tempList)

    decodeList = []                                                             # Create the list that is going to be used the decrypted code
    for letter in tempList1:
        if letter is not " ":                                                   # If not a blank space, find the chosen letter in the alphabet list, using index;
            position = alphabet.index(letter)
            indexFuture = position - shift                                      # Create the index that it will become by sum up with the "shift";
            decryptedLetter = alphabet [indexFuture]
            for letter in decryptedLetter:                                      # Add that new decryptedLetter in the decodeList;
                decodeList.append(letter)
        else:
            decodeList.append(letter)
    decodedWords = "".join(decodeList)                                          # Transform the list into a string

    print (decodedWords)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)


''' # Teacher's solution
def encrypt (plainText, shiftNumber):

    cipherText = ""

    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftNumber
        newLetter = alphabet[newPosition]
        cipherText += newLetter 
    print(cipherText)       
'''