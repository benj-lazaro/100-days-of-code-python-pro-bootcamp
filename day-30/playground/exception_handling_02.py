# Accept user height and weight
height = float(input("Height: "))
weight = float(input("Weight: "))

# Check for valid height (meters); raise your own exception
if height > 3:
    raise ValueError("Human height should NOT be more than 3 meters.")

# Calculate the BMI
bmi = weight / height ** 2
print(bmi)


