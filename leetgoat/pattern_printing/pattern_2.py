def pattern_2(num):
    for i in range(num):
        res = ""
        for j in range(i+1):
            res += "*"
        print(res)

pattern_2(4)