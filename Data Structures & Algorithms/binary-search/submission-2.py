class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            half_index = (left + right) // 2

            if nums[half_index] > target:
                right = half_index - 1
            elif nums[half_index] < target:
                left = half_index + 1
            else:
                return half_index

        return left if nums[left] == target else -1