def pattern_5(num):

    for i in range(num):
        res = ""
        for j in range(num-i):
            res += "*"
        print(res)

pattern_5(5)