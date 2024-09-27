
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars_cnt = defaultdict(int)
        res = 0
        is_odd = False
        for ch in s:
            chars_cnt[ch] += 1
            if chars_cnt[ch] % 2 == 0:
                res += 2

        for val in chars_cnt.values():
            if val%2 == 1:
                res += 1
                break
        return res

    def longestPalindrome(self, s: str) -> int:
        chars_seen = set()
        res = 0

        for c in s:
            if c in chars_seen:
                chars_seen.remove(c)
                res += 2
            else:
                chars_seen.add(c)

        return res + 1 if chars_seen else res


