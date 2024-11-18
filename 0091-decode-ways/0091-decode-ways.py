class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        for i in range(1, len(s) + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
                
            if i > 1 and (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6')):
                dp[i] += dp[i-2]
                
        return dp[-1]