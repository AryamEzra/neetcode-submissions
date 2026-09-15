class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        fixeds = ""
        for c in s:
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
                fixeds += c.lower()
            if c in check:
                fixeds += c

        # print(fixeds)
        l = 0
        r = len(fixeds) - 1
        while l <= r:
            if fixeds[l] == fixeds[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        