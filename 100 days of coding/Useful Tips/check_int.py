from multiprocessing.sharedctypes import Value
import time
from timeit import repeat


def check_int_123(number):
    while True:
        try:
            if(isinstance(number,int) and number in range(1,4)):
                print ("Valid answer!")
                break
            else:
                print("Invalid number")
                number = int(input("Type a valid number: "))
        except ValueError:
            print ("Please enter a valid number.")


def same_initial(wd1, wd2):
        """Tests if two words start with the same character,  
        and returns True/False. Case distinction is ignored.""" 
        if wd1[0].lower() == wd2[0].lower(): 
            return True