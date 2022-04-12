sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# Create a new dictionary that contains the word and its length from the given sentence
result = {word: len(word) for word in sentence.split()}

print(result)
