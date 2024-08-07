def pattern_11(n=5):

    for i in range(n):
        start = 0 if i%2 == 0 else 1
        for j in range(i+1):
            print(start, end="")
            start = 0 if start else 1
        print()

pattern_11()
