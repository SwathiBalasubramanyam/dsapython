class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        res_str = ""

        carry = 0
        for i in range(max_len-1, -1, -1):
            tsum = carry + int(a[i]) + int(b[i])
            carry = tsum // 2
            res_str = str(tsum%2) + res_str

        if carry:
            res_str = str(carry) + res_str

        return res_str
