def quick_sort(arr):
    if not arr or len(arr) == 1:
        return arr
    
    pivot = arr[0]
    left, right = [], []

    for ele in arr[1:]:
        if ele < pivot:
            left.append(ele)
        else:
            right.append(ele)

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([13, 46, 24, 52, 20, 9]))