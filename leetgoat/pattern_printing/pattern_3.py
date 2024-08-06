def pattern_3(num):

    for i in range(num):
        res = ""
        for j in range(i+1):
            res += str(j+1)
        print(res)

pattern_3(5)