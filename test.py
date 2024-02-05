class Solution:
    def sumOfSquares(self, nums):

        nums_len = len(nums)

        def filt_func(el):
            print(nums_len%el)
            if nums_len%el == 0:
                return el*el
            return 0

        return sum(map(filt_func, nums))
        

print(Solution().sumOfSquares([2,7,1,19,18,3]))

