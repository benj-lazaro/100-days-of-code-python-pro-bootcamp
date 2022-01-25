# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# Sample data = 180 124 165 173 189 169 146

height_sum = 0
student_count = 0

for student in student_heights:
    height_sum += student
    student_count += 1

average_height = height_sum / student_count

print(round(average_height))