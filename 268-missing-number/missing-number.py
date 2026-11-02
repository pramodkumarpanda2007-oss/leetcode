class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums)-1):
            p1 = i
            p2 = i+1

            if nums[p1]+1 == nums[p2]:
                continue
            else:
                return nums[p1]+1

        if nums[0] != 0:
            return 0

        return len(nums)
            