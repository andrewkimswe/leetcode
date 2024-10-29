class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        return list(res.values())
    
    
# 문자열 정렬 : O(M*NlogN)
# 문자 빈도수를 키로 사용 : O(M*N)