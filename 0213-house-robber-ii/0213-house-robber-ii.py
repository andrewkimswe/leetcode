class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums: List[int]) -> int:
            prev1, prev2 = 0, 0
            for num in nums:
                temp = prev1
                prev1 = max(prev1, prev2 + num)
                prev2 = temp
            return prev1

        case1 = rob_linear(nums[:-1])
        case2 = rob_linear(nums[1:])
        
        return max(case1, case2) 