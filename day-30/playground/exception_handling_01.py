# FileNoteFoundError
try:
    # Tries to open a file
    file = open("a_file.txt")

    # Tries to access the value of a non-existent dictionary key
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    # Creates a file in the event that it does not exist
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does NOT exists.")

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("This is an error that I made up.")
    # file.close()
    # print("File was closed.")
