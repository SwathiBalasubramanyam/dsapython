def vowel_cipher(string):
    # your code here
    vowels = "aeiou"

    new_word = ""
    for char in string:
        if char not in vowels:
            new_word += char
            continue
        idx = (vowels.index(char) + 1) % len(vowels)
        new_word += vowels[idx]

    return new_word


print(vowel_cipher("bootcamp")) # "buutcemp"
print(vowel_cipher("paper cup")) # "pepir cap"