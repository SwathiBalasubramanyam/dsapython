arr = [5,2,0,1]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                i -= 1
    return arr

print(insertion_sort(arr))