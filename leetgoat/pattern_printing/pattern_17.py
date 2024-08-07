def pattern_17(n=5):
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    prev_chars = ""
    for i in range(n):
        # spaces = n-1-i
        spres = ""
        for j in range(n-1-i):
            spres += " "

        char = ALPHABETS[i]
        print(spres + prev_chars + char + prev_chars[::-1] + spres)
        prev_chars += char

pattern_17()