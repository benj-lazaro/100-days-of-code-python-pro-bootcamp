PLACEHOLDER = "[name]"

# Opens & read the invited_names.txt and store individual entries as a list item
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Opens & read the starting_letter.txt
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    # Loop through each name entry & strip off the "\n" character
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        # Write the updated contents to a new file & save each file using the invitee's name as filename
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as complete_letter:
            complete_letter.write(new_letter)
