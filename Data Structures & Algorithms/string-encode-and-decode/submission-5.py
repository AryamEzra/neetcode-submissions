class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for c in strs:
            ans += c
            ans += "~"
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        cur = ""
        for i in s:
            if i != "~":
                cur += i
            else:
                ans.append(cur)
                cur = ""
        
        return ans
        
