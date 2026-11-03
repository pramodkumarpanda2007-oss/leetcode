class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] > 0:
                nums[index] *= -1

        l1 = []

        for i in range(len(nums)):
            if nums[i] > 0:
                l1.append(i + 1)

        return l1