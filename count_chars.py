
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import defaultdict
        count = 0
        char_to_cnt = defaultdict(int)
        for char in chars:
            char_to_cnt[char] += 1

        for word in words:
            can_form = True
            word_char_cnt = defaultdict(int)
            for char in word:
                if char not in char_to_cnt or word_char_cnt[char] >= char_to_cnt[char]:
                    can_form = False
                    break

                word_char_cnt[char] += 1

            if can_form:
                count += len(word)

        return count


print(Solution().countCharacters(["cat","bt","hat","tree"], "atach"))
        