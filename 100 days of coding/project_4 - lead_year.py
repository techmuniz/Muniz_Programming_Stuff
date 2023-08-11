print ("This program is to determine if the input is a leap year or not")

year = int(input("Type a year: "))

if year % 4 == 0:
    if year % 100 != 0:
        print ("It is a leap year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print ("It is a leap year")
        else:
            print ("It is not a leap year")
else:
    print ("It is not a leap year")



