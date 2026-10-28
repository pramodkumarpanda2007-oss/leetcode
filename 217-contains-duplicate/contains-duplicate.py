class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        res1=len(nums)
        res2=len(set(nums))
        if res1==res2:
            return False
        else:
            return True
    






        