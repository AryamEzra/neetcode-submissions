class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for d in digits:
            s += str(d)
        v = int(s)
        s = str(v + 1)
        ans = []
        for v in s:
            ans.append(int(v))
        return ans
        