
class Solution:
    def isHappy(self, n: int) -> bool:
        s1 = set()

        while n != 1 and n not in s1:
            s1.add(n)
            sum1 = 0

            while n > 0:
                d = n % 10
                sum1 += d ** 2
                n //= 10

            n = sum1

        return n == 1

        