class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = defaultdict(int)

        for ch in magazine:
            magazine_chars[ch] += 1


        for ch in ransomNote:
            if not magazine_chars.get(ch):
                return False

            magazine_chars[ch] -= 1

        return True