# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_ceiling = 90
current_age = int(age)
years = age_ceiling - current_age

days = years * 365
weeks = years * 52
months = years * 12

print(f'You have {days} days, {weeks} weeks, and {months} months left.')