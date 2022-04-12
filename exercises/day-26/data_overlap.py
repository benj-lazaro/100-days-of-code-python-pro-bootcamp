# Open the corresponding text files
with open("file1.txt") as file1:
    number_list_1 = file1.readlines()

with open("file2.txt") as file2:
    number_list_2 = file2.readlines()

# Use list comprehension to save common numbers between thw two files
result = [int(number) for number in number_list_1 if number in number_list_2]

# Write your code above 👆

print(result)
