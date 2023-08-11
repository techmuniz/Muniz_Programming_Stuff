

counter = 0

for number in range (1, 101):
    counter = counter + 1

    if counter % 3 == 0:
        if counter % 5 == 0:
            print ("FizzBuzz")
        else:
            print ("Fizz")
    
    elif counter % 5 == 0:
        print ("Buzz")
    
    else:
        print (counter)

