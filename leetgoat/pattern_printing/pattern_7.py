def pattern_7(num):

    for i in range(num):
        spres = ""
        for j in range(num-i-1):
            spres += " "
        
        stres = ""
        for j in range(2*i+1):
            stres += "*"

        print(spres + stres + spres)

pattern_7(5)