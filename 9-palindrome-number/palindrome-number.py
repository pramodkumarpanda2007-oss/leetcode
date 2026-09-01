class Solution:
    def isPalindrome(self, x: int) -> bool:
        t=x
        rev=0
        while x>0:
            d= x%10
            rev=rev*10+d
            x=x//10
        if(rev==t):
            return True
        else:
            return False
            
           
        