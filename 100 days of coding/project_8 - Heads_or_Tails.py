import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

dice_side = random.randint (0, 1)
if dice_side == 1:
    print ("Heads")
else:
    print ("Tails")














