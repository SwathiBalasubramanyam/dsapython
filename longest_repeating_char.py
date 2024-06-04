class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0
        max_len = 0
        char_cnt = defaultdict(int)

        for rp in range(len(s)):
            char_cnt[s[rp]] += 1

            most_freq_cnt = max(char_cnt.values())
            len_arr = rp-lp+1

            if len_arr - most_freq_cnt <= k:
                max_len = max(max_len, len_arr)
            else:
                char_cnt[s[lp]] -= 1
                lp += 1

        return max_len