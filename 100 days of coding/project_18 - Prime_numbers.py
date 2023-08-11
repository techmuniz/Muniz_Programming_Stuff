

def prime_checker(number):
    is_prime = True
    # if the number is divided by any other number than himself, variable changes to false, otherwise, it is a prime number
    for i in range (2, number):
        if number%i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)