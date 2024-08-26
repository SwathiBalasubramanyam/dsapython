# #     nums = [2,3,6,7,15]
# #     target = 9
'''the response should contain unique pair of indexes'''
# input --> list
# output --> list
# the pair should sum up to the target

nums = [2,3,6,7,15]
target = 9

def twoSum(ip_list, target):
    op_pairs = []
    for i in range(len(ip_list)):
        for j in range(i+1, len(ip_list)):
            if ip_list[i]+ip_list[j] == target and (i, j) not in op_pairs:
                op_pairs.append((i,j))
    return op_pairs


def twoSum2(ip_list, target):
    op_pairs = []
    seen_nos = {}
    for i in range(len(ip_list)):
        diff = target-ip_list[i]
        if diff in seen_nos:
            op_pairs.append((i, seen_nos[diff]))
        seen_nos[ip_list[i]] = i

    return op_pairs
print(twoSum2(nums, target))

