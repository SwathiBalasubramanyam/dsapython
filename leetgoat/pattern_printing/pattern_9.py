def pattern_9(n):

    for i in range(n):
        # space
        spres = ""
        for j in range(n-1-i):
            spres += " "

        #  stars
        stres = ""
        for j in range(2*i+1):
            stres += "*"

        print(spres + stres + spres)

    for i in range(n):
        # space
        spres = ""
        for j in range(i):
            spres += " "

        stres = ""
        for j in range(2*(n-1-i)+1):
            stres += "*"

        print(spres + stres + spres)

pattern_9(5)