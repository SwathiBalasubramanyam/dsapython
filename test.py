# class Solution:
#     def longestNiceSubstring(self, s: str) -> str:
#         from collections import Counter

#         stack = [s]
#         curr_max = ""
#         while stack:

#             last_ele = stack.pop()
#             char_cnt = Counter(last_ele)

#             for key in char_cnt.keys():
#                 if (key.islower() and not char_cnt.get(key.upper())) or (key.isupper() and not char_cnt.get(key.lower())):
#                     if len(last_ele[1:]) > 1: 
#                         stack.append(last_ele[1:])
#                     if len(last_ele[:-1]):
#                         stack.append(last_ele[:-1])

#                     break
#             else:
#                 if len(last_ele) > len(curr_max):
#                     curr_max = last_ele
                
            
#         return curr_max             
    
# print(Solution().longestNiceSubstring("YazaAay"))

# def hand_score(hand):
#     letters_points = {"A": 4, "K": 3, "Q": 2, "J": 1}
#     sum = 0
#     for ch in hand:
#         sum += letters_points[ch]
#     return sum

def sort_nums(nums):
	if not nums:
		return []
	
	pivot = nums[0]
	left = []
	right = []
	for ele in nums[1:]:
		if ele < pivot:
			left.append(ele)
		else:
			right.append(ele)
	return sort_nums(left) + [pivot] + sort_nums(right)

print(sort_nums([3,2,1]))