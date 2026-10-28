class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        count=0
        result=[]
        for i in accounts:
            for j in i:
                count+=j
            result.append(count)
            count=0   
        return max(result)

    


        