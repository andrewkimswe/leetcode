class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        result = [-1] * len(queries)
        min_heap = []
        i = 0

        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                if end >= q:
                    heapq.heappush(min_heap, (end - start + 1, end))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[idx] = min_heap[0][0]

        return result
