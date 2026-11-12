class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d={}
        for i in jewels:
            if i in  stones:
                key=i
                value=stones.count(i)
                d[key]=value
        sum1=0
        for i in d:
            sum1+=d[i]
        return sum1
        