class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count = Counter(t)
        required = len(t_count)
        
        left, right = 0, 0
        formed = 0
        window_count = {}
        
        min_length = float("inf")
        min_left, min_right = 0, 0
        
        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left, min_right = left, right

                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1

        return "" if min_length == float("inf") else s[min_left:min_right + 1]