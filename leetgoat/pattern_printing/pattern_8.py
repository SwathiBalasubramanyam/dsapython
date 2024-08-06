
def pattern_8(num):

    for i in range(num):
        # space
        spres = ""
        for j in range(i):
            spres += " "

        # stars
        stres = ""
        for j in range(2*(num-1-i)+1):
            stres += "*"

        print(spres + stres + spres)

pattern_8(5)