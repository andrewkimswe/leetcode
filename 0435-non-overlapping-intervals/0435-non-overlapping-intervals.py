class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        non_overlapping_count = 1
        last_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= last_end:
                non_overlapping_count += 1
                last_end = end

        return len(intervals) - non_overlapping_count
