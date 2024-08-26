with open('inputfiles/text.txt','r') as f, open('inputfiles/newfile.txt' ,"a+") as w:
    out = f.read().splitlines()

    for line in out:
        w.write(line + '\n')