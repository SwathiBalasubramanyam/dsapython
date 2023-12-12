def summation_sequence(start, length):
    # your code here
    res = [start]

    for i in range(1, length):
        res.append(sum([j for j in range(1, res[i-1]+1)]))

    return res

print(summation_sequence(3, 4)) # [3, 6, 21, 231]
print(summation_sequence(5, 3)) # [5, 15, 120]