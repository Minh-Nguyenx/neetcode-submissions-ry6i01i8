class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        return self.merge(left_half, right_half)
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]
        # Neu 1 trong 2 mang con sot lai cac phan tu (dong tren la viet gop 2 dong duoi)
        # result.extend(left[i:]) # result + left[i:]
        # result.extend(right[j:]) # result + right[j:]