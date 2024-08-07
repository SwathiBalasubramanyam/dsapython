def pattern_19(n=5):

    for i in range(n):
        for j in range(n-i):
            print("*", end="")

        for j in range(i*2):
            print(" ", end="")

        for j in range(n-i):
            print("*", end="")

        print()

    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        
        for j in range(2* (n-1-i)):
            print(" ", end="")

        for j in range(i+1):
            print("*", end="")

        print()

pattern_19()