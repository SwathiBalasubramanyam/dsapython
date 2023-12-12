# Feel free to use this variable:
# alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(string, num):
    # your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    new_word = ""
    for char in string:
        idx = (alphabet.index(char) + num) % 26
        new_word += alphabet[idx]

    return new_word

print(caesar_cipher("apple", 1))    # "bqqmf"
print(caesar_cipher("bootcamp", 2)) # "dqqvecor"
print(caesar_cipher("zebra", 4))    # "difve"