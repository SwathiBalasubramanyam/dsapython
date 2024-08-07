def pattern_12(n=5):

    for i in range(n):
        res = ""
        for j in range(i+1):
            res += str(j+1)

        for j in range(i+1, n):
            res += " "

        print(res + res[::-1])
        
pattern_12()