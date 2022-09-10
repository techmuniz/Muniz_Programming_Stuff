
# simple def-------------------------------------------------------------------------------
'''
def greet ():
    print("Hello")
    print("It's been a long time")
    print("Bye")

greet()
'''

# def with one input-----------------------------------------------------------------------
'''
def greet_with_name(name):
    print (f"Hello {name}")
    print (f"How're you doing {name}?")

greet_with_name("Paulo")
'''

# def with more than 1 input----------------------------------------------------------------
'''
def greet_name_city(name, city):
    print(f"Hello {name}, I see that your are from {city}")

greet_name_city("Paulo", "Bangu")
'''


# def using Keywords arguments--------------------------------------------------------------


def greet_name_city(name, city, weather):
    print(f"Hello {name}, I see that your are from {city}. the weather seems {weather} today")

greet_name_city(name="Paulo", city="Bangu", weather="fine")