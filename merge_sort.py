# Write your code here.
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(first_half, second_half):
    new_arr = []
    
    while first_half and second_half:
        if first_half[0] <= second_half[0]:
            new_arr.append(first_half[0])
            first_half = first_half[1:]
        else:
            new_arr.append(second_half[0])
            second_half = second_half[1:]

    return new_arr + first_half + second_half


lst = [5, 2, 38, 91, 16, 427]

sorted_lst = merge_sort(lst)        # Out of place solution
print(sorted_lst)
