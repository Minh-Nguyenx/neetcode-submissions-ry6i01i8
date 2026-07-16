class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            x = nums[i]
            j = target - x
            if j in seen:
                return [seen[j], i]
            else:
                seen[x] = i