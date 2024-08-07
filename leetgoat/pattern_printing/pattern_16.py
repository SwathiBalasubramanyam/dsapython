def pattern_16(n=5):
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(i+1):
            print(ALPHABETS[i], end="")

        print()

pattern_16()