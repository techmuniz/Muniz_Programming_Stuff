# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

'''Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?'''

highnumber = 0

for n in student_scores:
    if n > highnumber:
        highnumber = n
    else:
        continue

print(f"The highest score in the class is: {highnumber}")
