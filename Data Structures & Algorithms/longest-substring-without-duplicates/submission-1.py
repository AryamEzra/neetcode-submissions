class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        check = set()
        for r in range(len(s)):
            if s[r] not in check:
                check.add(s[r])
            else:
                while s[r] in check:
                    check.remove(s[l])
                    l += 1
                check.add(s[r])
            # print(check)
            ans = max(ans, r-l+1)

        return ans

        