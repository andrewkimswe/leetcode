class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x*x + y*y, [x,y]) for x,y in points]
        heapq.heapify(heap)
        
        return [point for dist, point in heapq.nsmallest(k, heap)]