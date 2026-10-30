class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        for i in s:
            if i.isalnum():
                s1+=i
        s2=s1.lower()
        p=s2[::-1]
        if s2==p:
          return True
        else:
          return False
        