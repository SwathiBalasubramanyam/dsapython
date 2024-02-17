class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        from collections import Counter

        stack = [s]
        curr_max = ""
        while stack:

            last_ele = stack.pop()
            char_cnt = Counter(last_ele)

            for key in char_cnt.keys():
                if (key.islower() and not char_cnt.get(key.upper())) or (key.isupper() and not char_cnt.get(key.lower())):
                    if len(last_ele[1:]) > 1: 
                        stack.append(last_ele[1:])
                    if len(last_ele[:-1]):
                        stack.append(last_ele[:-1])

                    break
            else:
                if len(last_ele) > len(curr_max):
                    curr_max = last_ele
                
            
        return curr_max             
    
print(Solution().longestNiceSubstring("YazaAay"))