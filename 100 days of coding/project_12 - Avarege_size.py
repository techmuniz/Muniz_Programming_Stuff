#Forbidden to use sum() or len()!!!!

 # 🚨 Don't change the code below 👇

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆
#Write your code below this row 👇

soma = float()
counter = float()

for x in student_heights:
    soma = soma + x

for x in student_heights:
    counter = counter + 1

avarege = round(soma // counter)

print (avarege)

