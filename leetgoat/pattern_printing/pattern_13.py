
def pattern_13(n=5):
    start = 1

    for i in range(n):
        for j in range(i+1):
            print(start, end="")
            start += 1

        print()


pattern_13()