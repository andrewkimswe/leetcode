class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k == 1:
            return nums

        deq = deque()
        result = []

        for i in range(k):
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)

        for i in range(k, len(nums)):
            result.append(nums[deq[0]])

            while deq and deq[0] <= i - k:
                deq.popleft()

            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()

            deq.append(i)

        result.append(nums[deq[0]])

        return result