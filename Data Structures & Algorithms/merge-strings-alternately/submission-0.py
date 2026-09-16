class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        ans = ""
        for i in range(l):
            ans += word1[i]
            ans += word2[i]
        
        if len(word1) > len(word2):
            ans += word1[l:]
        else:
            ans += word2[l:]
        return ans
        