class Solution:
    def minEatingSpeed(self, piles, h):
        
        import math
        max_bananas = max(piles)
        
        completed = []
        for idx in range(1, max_bananas+1):
            hours_so_far = 0
            for pile in piles:
                hours_so_far += math.ceil(pile/idx)

            if hours_so_far <= h:
                completed.append(idx)

        return min(completed)

print(Solution().minEatingSpeed([3,6,7,11], 8))