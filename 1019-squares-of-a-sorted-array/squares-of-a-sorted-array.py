class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l1=[]
        for i in nums:
            l1.append(i**2)
        l1.sort()
        return l1
        