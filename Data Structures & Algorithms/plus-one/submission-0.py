class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = ""
        for v in digits:
            d += str(v)
        i = int(d)
        i += 1
        s = str(i)
        ans = []
        for c in s:
            ans.append(c)
        return ans
        