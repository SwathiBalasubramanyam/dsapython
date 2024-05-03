arr = [5, 2, 38, 91, 16, 427]

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    def sort_left_right(left_arr, right_arr):
        res_arr = []
        while len(left_arr) and len(right_arr):
            
            if left_arr[0] < right_arr[0]:
                res_arr.append(left_arr[0])
                left_arr = left_arr[1:]
            else:
                res_arr.append(right_arr[0])
                right_arr = right_arr[1:]

        return res_arr + left_arr + right_arr
    
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    return sort_left_right(merge_sort(left_arr), merge_sort(right_arr))

print(merge_sort(arr))