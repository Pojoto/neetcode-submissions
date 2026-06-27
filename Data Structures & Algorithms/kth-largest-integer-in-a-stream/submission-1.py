class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort()
        self.k = k

    def add(self, val: int) -> int:
        insert_spot = len(self.nums)
        for i, num in enumerate(self.nums):
            if val < num:
                insert_spot = i
                break
        self.nums.insert(insert_spot, val)
        
        return self.nums[-self.k]

