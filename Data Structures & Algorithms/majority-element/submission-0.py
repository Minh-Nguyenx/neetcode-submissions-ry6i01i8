class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        n = len(nums)

        for i in nums:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1

            if counts[i] > n // 2:
                return i


