nums = [100,200,100,100,-200]
# import heapq
# res = heapq.nlargest(3,nums)
# print (res)

def bubble_sort(nums):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                sorted = False

def quick_sort(nums):
    if not nums :
        return nums
    pivot = nums[0]
    left, right = [], []
    for num in nums[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(nums):
    if not nums or len(nums) == 1:
        return nums
    
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]

    return sort_list(merge_sort(left), merge_sort(right))

def sort_list(left_arr, right_arr):
    combined_arr = []
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            combined_arr.append(left_arr[0])
            left_arr = left_arr[1:]
        else:
            combined_arr.append(right_arr[0])
            right_arr = right_arr[1:]
    if left_arr:
        combined_arr += left_arr
    if right_arr:
        combined_arr += right_arr

    return combined_arr

print(merge_sort(nums))




