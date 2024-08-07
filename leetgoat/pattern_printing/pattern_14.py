def pattern_14(n=5):
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(i+1):
            print(ALPHABETS[j], end="")

        print()

pattern_14()