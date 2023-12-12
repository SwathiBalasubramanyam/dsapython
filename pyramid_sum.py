def pyramid_sum(base):
    # your code here
    new_lst = []

    while base:
        new_lst = [base] + new_lst
        base = adjacent_sum(base)

    return new_lst

def adjacent_sum(lst):
    new_lst = []

    for i in range(1, len(lst)):
        new_lst.append(lst[i] + lst[i-1])

    return new_lst

print(pyramid_sum([1, 4, 6])) # [[15], [5, 10], [1, 4, 6]]
print(pyramid_sum([3, 7, 2, 11])) # [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]