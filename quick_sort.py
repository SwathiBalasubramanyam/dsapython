def quick_sort(lst):

    if not lst:
        return lst

    pivot = [lst[0]]
    left_eles = []
    right_eles = []

    for ele in lst[1:]:
        if ele <= lst[0]:
            left_eles.append(ele)
        else:
            right_eles.append(ele)

    return quick_sort(left_eles) + pivot + quick_sort(right_eles)


lst = [5, 2, 38, 91, 16, 427]
print(quick_sort(lst))