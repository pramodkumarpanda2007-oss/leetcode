
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum1 = 0
        max1 = float('-inf')

        for i in nums:
            sum1 += i

            if sum1 > max1:
                max1 = sum1

            if sum1 < 0:
                sum1 = 0

        return max1


        