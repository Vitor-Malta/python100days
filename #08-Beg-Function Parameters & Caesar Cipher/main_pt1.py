alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    shift_counter = 0
    shifted_alphabet = []
    for i in range(0, len(alphabet)):
        if i + shift_amount < len(alphabet):
            shifted_alphabet += alphabet[i + shift_amount]
        else:
            shifted_alphabet += alphabet[shift_counter]
            shift_counter += 1
    encrypted_text = ""
    for i in range(len(plain_text)):
        encrypted_text += shifted_alphabet[alphabet.index(plain_text[i])]
    return print(encrypted_text)


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#  and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt
#  a message.
encrypt(plain_text=text, shift_amount=shift)
