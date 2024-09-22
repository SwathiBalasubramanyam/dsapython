# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lp, rp = 1, n

        while lp < rp:
            mid = (lp+rp) // 2

            if isBadVersion(mid):
                rp = mid
            else:
                lp = mid + 1

        return lp


