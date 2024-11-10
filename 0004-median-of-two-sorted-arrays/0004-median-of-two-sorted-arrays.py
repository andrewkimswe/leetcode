class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2

        left, right = 0, m
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

            max_left1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            min_right1 = nums1[mid1] if mid1 < m else float('inf')
            
            max_left2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            min_right2 = nums2[mid2] if mid2 < n else float('inf')

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 1:
                    return max(max_left1, max_left2)
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            
            elif max_left1 > min_right2:
                right = mid1 - 1
            else:
                left = mid1 + 1
