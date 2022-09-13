

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (text, shift):
    temp_list = []                                                              # Create a list do transform the input text into a list of separeted characters.
    for letter in text:
        temp_list.append(letter)
    
    encoded_list = []                                                           # Create the list that is going to be used the encripted code
    for letter in temp_list:
        if letter is not " ":                                                   # If not a blank space, find the chosen letter in the alphabet list, using index;
            position = alphabet.index(letter)                                   
            indexNumberFuture = position + shift                                # Create the index that it will become by sum up with the "shift";
            encriptedLetter= alphabet[indexNumberFuture]                        
            for letter in encriptedLetter:                                      # Add that new encriptedLetter in the encoded_list;
                encoded_list.append(letter)
        else:                                                                   # Exception created for the black space
            encoded_list.append(letter)
    
    encodedWords = "".join(encoded_list)                                        # Transform the list into a string

    print (encodedWords)                                                        # The result is a encoded phrase


'''def encrypt (plainText, shiftNumber):

    cipherText = ""

    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftNumber
        newLetter = alphabet[newPosition]
        cipherText += newLetter 
    print(cipherText)       
'''
encrypt(text, shift)
