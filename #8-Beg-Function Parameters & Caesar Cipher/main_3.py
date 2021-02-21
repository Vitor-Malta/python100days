alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(plain_text, shift_amount, choosen_direction):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if choosen_direction == "encode":
            new_position = position + shift_amount
        elif choosen_direction == "decode":
            new_position = position - shift_amount
        else:
            return print("Something is wrong. ERROR 101")
        cipher_text += alphabet[new_position]
    print(f"The {choosen_direction} text is {cipher_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text=text, shift_amount=shift, choosen_direction=direction)
