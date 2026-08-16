class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for c in strs:
            ans += c
            ans += "~"
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        l = len(s)
        ans = []
        i = 0
        while i < l:
            j = i
            while j < l and s[j] != "~":
                j += 1
            ans.append(s[i:j])
            i = j + 1
        
        return ans
        
