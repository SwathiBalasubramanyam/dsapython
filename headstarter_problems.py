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