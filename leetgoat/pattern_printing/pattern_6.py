def pattern_6(num):

    for i in range(num):
        res = ""
        for j in range(num-i):
            res += str(j+1)
        print(res)

pattern_6(5)