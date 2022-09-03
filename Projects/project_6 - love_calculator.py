# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

total_name1truecount = name1_lowercase.count ("t") + name1_lowercase.count("r") + name1_lowercase.count("u") + name1_lowercase.count("e")
total_name2truecount = name2_lowercase.count ("t") + name2_lowercase.count("r") + name2_lowercase.count("u") + name2_lowercase.count("e")

total_name1lovecount = name1_lowercase.count ("l") + name1_lowercase.count("o") + name1_lowercase.count("v") + name1_lowercase.count("e")
total_name2lovecount = name2_lowercase.count ("l") + name2_lowercase.count("o") + name2_lowercase.count("v") + name2_lowercase.count("e")

total_true = total_name1truecount + total_name2truecount
total_love = total_name1lovecount + total_name2lovecount

result_in_str = str(total_true)+str(total_love)
result_in_int = int(result_in_str)

if result_in_int < 10 or result_in_int > 90:
    print (f"Your score is {result_in_int}, you go together like coke and mentos.")
elif result_in_int >= 40 and result_in_int <= 50:
    print (f"Your score is {result_in_int}, you are alright together.")
else:
    print (f"Your score is {result_in_int}.")