class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        lst=[]
        for i in range(len(nums)):
            lst.append(nums[nums[i]])
        return lst

        