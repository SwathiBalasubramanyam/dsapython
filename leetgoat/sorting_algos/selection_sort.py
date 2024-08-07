def selection_sort(arr):
    # find minimum in array and swap
    
    for i in range(len(arr)-1):
        min_index, min_so_far = None, float("inf")
        for j in range(i, len(arr)):
            if arr[j] < min_so_far:
                min_index, min_so_far = j, arr[j]

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print(arr)

selection_sort([13, 46, 24, 52, 20, 9])