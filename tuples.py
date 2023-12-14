# DO NOT EDIT
odds = (1,3,5,7,9)
evens = (2,4,6,8)

# Step 1: Print out the result of adding evens to odds

print(odds+evens)

# Step 2: Print out the result of multiplying odds by three

print(odds*3)

# Step 3A: Use print to find out if odds is less than evens

print(odds < evens)

# Step 3B: Print out your explanation of why 3A has that result
# bcoz first item in the tuple/list is less than the first item in the evens tuple/list

# Step 4: Print out the average of the numbers in evens using one line of code
print(sum(evens)/len(evens))

# Step 5A: Write a function 'minmaxmean' that accepts an iterable and
#         returns the minimum value, the maximum value and the average (mean)

def minmaxmean(tp):
    return min(tp), max(tp), sum(tp)/len(tp)


# Step 5B: Use print to confirm you function is working on evens and odds

print(minmaxmean(odds))


# BONUS: Call your function with a new tuple of your own creation
#        And print the results in a pretty way


def add_value(tp, val):
    return tp + (val,)


print(add_value((1,2,3,4), 5)) #> (1, 2, 3, 4, 5)
print(add_value(("a", "b", "c"), "d")) #> ('a', 'b', 'c', 'd')
print(add_value((8, 9, "d", 6), "a")) #> (8, 9, 'd', 6, 'a')

# Write your function, here.

def big_words(tp):
    return tuple([ele for ele in tp if len(ele) > 8])



print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
print(big_words(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')


# Write your function, here.
def recursive_add(tp):
    if not tp:
        return 0

    return tp[0] + recursive_add(tp[1:])



print(recursive_add((2, )))               #> 2
print(recursive_add((2, 4, 6, 8, 10)))    #> 30
print(recursive_add((25, 50, 75, 100)))   #> 250

# Write your function, here.

def index_sort(lst):
    return sorted(lst, key=lambda item: item[1])


print(index_sort([(1, 2, 3), (6, 8, 9), (0, 5, 0), (2, 0, 4)])) #> [(2, 0, 4), (1, 2, 3), (0, 5, 0), (6, 8, 9)]
print(index_sort([(9, 55, 11), (7, 14, 5), (32, 41, 12), (8, 5, 2)])) #> [(8, 5, 2), (7, 14, 5), (32, 41, 12), (9, 55, 11)]
print(index_sort([(0, 9, 1), (4, 3, 0), (6, 5, 14), (64, 32, 28)])) #> [(4, 3, 0), (6, 5, 14), (0, 9, 1), (64, 32, 28)]

# Write your function, here.
def bubble_sum(lst):
    return sorted(lst, key=lambda item: sum(item))


print(bubble_sum([(3, 5), (1, 3), (6, 5), (2, 8)])) #> [(1, 3), (3, 5), (2, 8), (6, 5)]
print(bubble_sum([(2, 5), (2, 5), (7, 8), (2, 6)])) #> [(2, 5), (2, 5), (2, 6), (7, 8)]
print(bubble_sum([(5, 6), (1, 2), (3, 0), (2, 4)])) #> [(1, 2), (3, 0), (2, 4), (5, 6)]
print(bubble_sum([(5, 4), (1, 0), (2, 1), (4, 1)])) #> [(1, 0), (2, 1), (4, 1), (5, 4)]

from itertools import combinations

print("*"*100)

for ele in combinations([2,3,4,6], 4):
    print(ele)

def encode(lst):
    res = ""
    for ele in lst:
        res += str(len(ele)) + "#" + ele
    return res

def decode(str):

    res, i = [], 0

    while i < len(str):
        j = i

        while str[j] != "#":
            j += 1

        length = int(str[i:j])
        res.append(str[j+1: j+1+length])        
        i = j+1+length
    return res


print("*"*100)


print(decode(encode(["neet", "code"])))
