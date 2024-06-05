def sum67(nums):
    res = 0
    seen_six = False

    for num in nums:
        if num in [6, 7]:
            seen_six = num == 6
            continue

        if not seen_six:
            res += num

    return res



print(sum67([1,2,2,6,99, 99,7, 2]))

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(s):
    cat_cnt = 0
    dog_cnt = 0

    for i in range(len(s)-(len("cat")-1)):
        sub_str = s[i:i+3]
        if sub_str == "cat":
            cat_cnt += 1
        elif sub_str == "dog":
            dog_cnt += 1

    return cat_cnt == dog_cnt

print(cat_dog("1cat1cadodog"))

def find_id_pair(nums, target):
    num_to_id = {}
    for idx, num in enumerate(nums):
        component = target - num

        if component in num_to_id and num_to_id[component] != idx:
            return [idx, num_to_id[component]]
        
        num_to_id[num] = idx
        

# Example 1:
# - Input: nums = [2, 7, 11, 15], target = 9
# - Output: [0, 1]
print(find_id_pair([2, 7, 11, 15], 9))

# Example 2:
# - Input: nums = [3, 2, 4], target = 6
# - Output: [1, 2]
print(find_id_pair([3,2,4], 6))

# Example 3:
# - Input: nums = [3,3], target = 6
# - Output: [0,1]
print(find_id_pair([3,3], 6))
