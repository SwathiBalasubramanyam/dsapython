def pattern_18(n=5):
    ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        for j in range(n-1-i, n):
            print(ALPHABETS[j], end="")

        print()

pattern_18()