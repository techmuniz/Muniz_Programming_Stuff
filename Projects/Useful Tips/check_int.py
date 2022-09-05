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
            
            
            
choice1 = int(input("What's your choice? 1, 2 or 3?\n"))

check_int_123(choice1)
