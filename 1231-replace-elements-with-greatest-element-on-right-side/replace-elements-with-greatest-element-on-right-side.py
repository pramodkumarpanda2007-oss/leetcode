class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        l1 = []
        max1 = -1

        for i in range(len(arr)-1, -1, -1):
            l1.append(max1)

            if arr[i] > max1:
                max1 = arr[i]

        return l1[::-1]