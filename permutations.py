class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]

        res = []
        perms = self.permute(nums[1:])
        for perm in perms:
            for i in range(len(perm)+1):
                res.append(perm[:i] + [nums[0]] + perm[i:])
        return res


        # backtracking solution
        # if len(nums) == 1:
        #     return [nums[:]]

        # res = []

        # for i in range(len(nums)):
        #     n = nums.pop(0)
        #     perms = self.permute(nums)

        #     for perm in perms:
        #         perm.append(n)
        #     res += perms

        #     nums.append(n)

        # return res
        

print(Solution().permute([1,2,3]))