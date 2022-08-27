#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

from timeit import repeat


print ('Welcome to the Tip Calculator 5000')

#check if is numeric
bill = input("What was the total bill value?\n")

while bill.isnumeric() == False:
    print ("error\n")
    bill = input("Please, input the correct total bill value?\n")
else:
    pass


#Test for preventing people from using something that is not the options that I want.
tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")

while tip.isnumeric() == False:
    print("Please, insert a valid number")
    tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
else:
    pass
while int(tip) not in (10, 12, 15):
    print("Error, insert a valid number!")
    tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
else:
    pass


#Check how many people is going to pay up. If the number is not int, gives an error. If response is not numeric, keep trying
people = input("How many people to split the bill? ")

while people.isnumeric() == False:
    print ("error\n")
    people = input("How many people to split the bill?\nPlease, type a valid number: ")
else:
    print (people)

#Final calculations
individual_tip = (int(bill)/int(people))*(int(tip)/100)
total_payment = (int(bill)/int(people)) + individual_tip

print (f"Total tip price is ${round(individual_tip, 2)}")
print (f"Total value for each, with the tip is ${round(total_payment, 2)}")


















