def adjacent_sum(num_list):
    # your code here

    new_lst = []

    for i in range(1, len(num_list)):
        new_lst.append(num_list[i] + num_list[i-1])

    return new_lst

print(adjacent_sum([3, 7, 2, 11])) # [10, 9, 13], because [ 3+7, 7+2, 2+11 ]
print(adjacent_sum([2, 5, 1, 9, 2, 4])) # [7, 6, 10, 11, 6], because [2+5, 5+1, 1+9, 9+2, 2+4]