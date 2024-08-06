def pattern_4(num):

    for i in range(num):
        res = ""
        for j in range(i+1):
            res += str(i+1)
        print(res)

pattern_4(5)