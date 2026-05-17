class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = []
        for c in s:
            if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
                check.append(c.lower())
        # print(check)
        return check == check[::-1]
            