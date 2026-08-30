class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        def sum_square(n):
            ans = 0
            while n > 0:
                rem = n % 10
                n = n // 10
                ans += (rem ** 2)
            return ans
            
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = sum_square(n)
        return True



        