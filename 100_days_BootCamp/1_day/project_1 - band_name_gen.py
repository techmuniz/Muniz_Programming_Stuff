#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

#1. Create a greeting for your program.
print ("So... you got the band, but you got no name for it? Let me help you out!")

#2. Ask the user for the city that they grew up in.
city_name = input("What is the name of the city you were born? \n")

#3. Ask the user for the name of a pet.
pet_name = input("What about your favourite pet's name: \n")

#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + " " + pet_name

#5. Make sure the input cursor shows on a new line, see the example at:
print (f"A good name for your band would be {band_name}")