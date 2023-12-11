def cap_space(str):

    words = []
    word = ""
    for idx, char in enumerate(str):
        if char.isupper():
            words.append(word)
            word  = char.lower()
        else:
            word += char

    words.append(word)
    
    return " ".join(words)

print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"