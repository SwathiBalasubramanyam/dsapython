def consonant_cancel(sentence):
    res = []
    for word in sentence.split(" "):
        for idx, char in enumerate(word):
            if char in "aeiou":
                res.append(word[idx:])
                break

    return " ".join(res)

print(consonant_cancel("down the rabbit hole")) # "own e abbit ole"
print(consonant_cancel("writing code is challenging")) # "iting ode is allenging"