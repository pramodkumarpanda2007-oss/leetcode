class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        cnt=0
        max1=0
        for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    cnt+=1
                    max1=max(cnt,max1)
                elif nums[i]>=nums[i+1]:
                    cnt=0
        return max1+1
            
                