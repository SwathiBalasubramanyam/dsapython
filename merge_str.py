class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        my_big_str = ""

        while word1 and word2:
            my_big_str += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]

        if word1:
            my_big_str += word1

        if word2:
            my_big_str += word2

        return my_big_str
        