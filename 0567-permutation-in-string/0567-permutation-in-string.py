class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])

        if s1_count == window_count:
            return True

        for i in range(len1, len2):
            window_count[s2[i]] += 1
            
            left_char = s2[i - len1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            if s1_count == window_count:
                return True

        return False
