
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum1 = 0

        for i in range(k):
            sum1 += nums[i]

        max1 = sum1

        for i in range(k, len(nums)):
            sum1 += nums[i] - nums[i-k]
            max1 = max(max1, sum1)

        return max1 / k

        