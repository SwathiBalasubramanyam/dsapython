def triple_sequence(start, length): 
    # your code here
    res = [start]

    for i in range(1, length):
        res.append(res[i-1]*3)

    return res

print(triple_sequence(2, 4)) # [2, 6, 18, 54]
print(triple_sequence(4, 5)) # [4, 12, 36, 108, 324]