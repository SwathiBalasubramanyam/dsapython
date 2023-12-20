# Write your function, here.

def difference(lst):
    return max(lst) - min(lst)

print(difference([10, 15, 20, 2, 10, 6]))
# 20 - 2 = 18

print(difference([-3, 4, -9, -1, -2, 15]))
# 15 - (-9) = 24

print(difference([4, 17, 12, 2, 10, 2]))
# 17 - 2 = 15


# Write your function, here.
import random

def rng(lst):

    while len(lst) < 100 :
        rand = random.randint(0, 100)
        if rand not in lst:
            lst.append(rand)

    return lst

print(rng([]))