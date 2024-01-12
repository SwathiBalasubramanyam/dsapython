class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        prefix_in_all = False

        while prefix and not prefix_in_all:
            prefix_in_all = True
            for ele in strs[1:]:   
                if ele:
                    prefix_in_all = False
                    prefix = prefix[:-1]
                    break


        return prefix


print(Solution().longestCommonPrefix(["c","acc","ccc"]))