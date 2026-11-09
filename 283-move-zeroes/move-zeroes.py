class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
            count = 0
            j = len(nums)

            for i in range(j):
                if nums[i] == 0:
                    count += 1

            nums[:] = [i for i in nums if i != 0]

            while count > 0:
                nums.append(0)
                count -= 1

            return nums
        