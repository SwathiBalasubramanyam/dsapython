
def pattern_10(n=5):
    
    for i in range(2*n):
        res = ""
        if i < n-1:
            for j in range(i+1):
                res += "*"
        else:
            for j in range(2*n-i):
                res += "*"

        print(res)

pattern_10()