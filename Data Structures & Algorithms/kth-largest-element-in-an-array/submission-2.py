class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        larges = []

        for num in nums:
                
            if (len(larges) < k) or (len(larges) > 0 and num > larges[-1]):
                left = 0
                right = len(larges)
                while left < right:
                    half_index = (left + right) // 2

                    if larges[half_index] > num:
                        left = half_index + 1
                    else:
                        right = half_index

                larges.insert(left, num)

                if len(larges) > k:
                    larges.pop()        
        return larges[-1]

