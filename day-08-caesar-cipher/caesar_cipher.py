alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def  caesar(direction, text, shift):
    if direction == "encode":
        max_index = 25
        cipher_text = ""

        for character in text:
            current_position = alphabet.index(character)
            new_position = current_position + shift

            if current_position >= max_index:
                current_position = 0
                new_position = current_position + shift - 1

            if current_position + shift > max_index:
                difference_index = max_index - current_position
                current_position = 0
                new_position = (shift - difference_index) + current_position - 1

            cipher_text += alphabet[new_position]

        print(f"The encoded text is {cipher_text}")

    else:
        clear_text = ""

        for character in text:
            current_position = alphabet.index(character)
            new_position = current_position - shift
            clear_text += alphabet[new_position]

        print(f"The decoded text is {clear_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(direction, text, shift)
