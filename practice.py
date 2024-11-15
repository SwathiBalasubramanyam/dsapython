
def bubblesort(arr):

    arr_sorted = False

    while not arr_sorted:
        arr_sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                arr_sorted = False
                break
    return arr

def quicksort(arr):
    if not arr:
        return arr

    pivot = arr[0]
    left_arr = [el for el in arr[1:] if el < pivot]
    right_arr = [el for el in arr[1:] if el > pivot]

    return quicksort(left_arr) + [pivot] + quicksort(right_arr)


print(quicksort([7,1,5,3,6,4]))

