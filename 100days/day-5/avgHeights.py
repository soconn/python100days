# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
a=0
b=0
for i in student_heights:
    a+=1
    b=b+i

c=b/a
print("total students: " + str(a))
print("total height: " + str(b))
print("average height " + str(c))

