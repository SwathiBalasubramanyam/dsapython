def pattern_22(n=5):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top, left, bottom, right = i, j, (2*n-1)-1-i, (2*n-1)-1-j
            distance = min(top, left, bottom, right)
            print(n-1-distance, end="")
        print()


pattern_22()
