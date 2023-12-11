class Solution:
    def addBinary(self, a: str, b: str) -> str:
        my_dict = {
            "11": ["0", "1"],
            "01": ["1", "0"],
            "10": ["0", "0"],
            "00": ["0", "0"]
        }

        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0

        new_str = ""

        for idx in range(max_len-1, -1, -1):
            total, curr_carry = my_dict[a[idx]+b[idx]]
            new_str += total
        
        new_str = curr_carry + new_str
        return new_str

print(Solution().addBinary("1", "1"))