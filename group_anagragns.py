from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        sorted_str_to_ele = defaultdict(list)

        for word in strs:
            str_list = list(word)
            str_list.sort()
            sorted_str_to_ele["".join(str_list)] += [word]

        return sorted_str_to_ele.values()

        
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))