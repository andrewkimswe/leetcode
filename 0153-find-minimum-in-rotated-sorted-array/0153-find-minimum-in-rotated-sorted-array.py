class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end )
            curr_min = min(curr_min,nums[mid])
            
            if nums[mid] > nums[end]:
                start = mid + 1
                
            else:
                end = mid - 1
                
        return min(curr_min,nums[start])
