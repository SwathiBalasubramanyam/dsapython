def pattern_15(n=5):
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(n-i):
            print(ALPHABETS[j], end="")

        print()

pattern_15()