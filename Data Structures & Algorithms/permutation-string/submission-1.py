class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window to check letters
        # hashmap to store frequencies (letter counter is constant space since 26 letters)
        if len(s1) > len(s2):
            return False

        l, r = 0, 0
        s1_map = Counter(s1) 
        s2_map = {}
        
        while r < len(s2):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            if s2_map == s1_map:
                return True
            
            if r - l + 1 >= len(s1):
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l += 1
            r += 1
            
        return False
