def merge_sort(arr):
    if not arr or len(arr) == 1:
        return arr
    mid = len(arr)//2
    return sort_arr(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def sort_arr(left_arr, right_arr):
    res = []
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            res.append(left_arr[0])
            left_arr = left_arr[1:]
        else:
            res.append(right_arr[0])
            right_arr = right_arr[1:]

    return res + left_arr + right_arr

print(merge_sort([13, 46, 24, 52, 20, 9]))