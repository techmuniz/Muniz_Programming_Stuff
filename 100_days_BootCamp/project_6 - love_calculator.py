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

result_in_str = {str(total_true)+str(total_love)}



print (f"Total 'True' numbers in first name is {total_name1truecount}, and for the second name is {total_name2truecount},\n combining a total or {total_true}.")
print (f"Total 'Love' number in first name is {total_name1lovecount}, and for the second name is {total_name2lovecount}, \n combining a total of {total_love}")


print (f"Your score is {result_in_str} in string, and X in int.")
