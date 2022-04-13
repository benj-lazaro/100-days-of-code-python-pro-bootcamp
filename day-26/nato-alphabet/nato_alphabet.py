import pandas

# Read the CSV file containing the NATO alphabet
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format {"A": "Alfa", "B": "Bravo"}:
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

# Use list comprehension to find the corresponding phonetic for each letter of the given word
nato_list = [nato_dict[letter] for letter in user_word]
print(nato_list)
