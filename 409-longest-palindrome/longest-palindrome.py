
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        
        for i in s:
            count[i] = count.get(i, 0) + 1
        
        sum1 = 0
        odd = False
        
        for i in count.values():
            if i % 2 == 0:
                sum1 += i
            else:
                sum1 += i - 1
                odd = True
        
        if odd:
            sum1 += 1
        
        return sum1
