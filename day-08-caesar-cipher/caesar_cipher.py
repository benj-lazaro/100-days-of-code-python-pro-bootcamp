alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def  encrypt(plain_text, shift_value):
    cipher_text = ""

    for letter in plain_text:
        letter_index = alphabet.index(letter)
        cipher_letter_index = letter_index + shift_value

        # Wrap around the alphabet list index to the beginning item it reached the last element
        if (letter_index >= 25):
            letter_index = 0
            cipher_letter_index = letter_index + shift_value - 1

        cipher_letter = alphabet[cipher_letter_index]
        cipher_text += cipher_letter

    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def  decrypt(cipher_text, shift_value):
    clear_text = ""

    for letter in cipher_text:
        cipher_index = alphabet.index(letter)
        clear_letter_index = cipher_index - shift_value

        # Wrap around the alphabet list index to the beginning item it reached the first element
        if (cipher_index <= 0):
            cipher_index = 25
            clear_letter_index = cipher_index - shift_value + 1

        clear_letter = alphabet[clear_letter_index]
        clear_text += clear_letter

    print(f"The decoded text is {clear_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if (direction.lower() == "encode"):
    encrypt(plain_text=text, shift_value=shift)
else:
    decrypt(cipher_text=text, shift_value=shift)
