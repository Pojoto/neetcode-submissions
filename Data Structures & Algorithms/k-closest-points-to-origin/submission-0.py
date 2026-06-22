class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for point in points:

            distance = math.sqrt(point[0]**2 + point[1]**2)

            heapq.heappush(heap, (-distance, point))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        
        for i, point_tuple in enumerate(heap):
            heap[i] = point_tuple[1]
        
        return heap
