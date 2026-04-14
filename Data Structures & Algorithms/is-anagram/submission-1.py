class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use hashmap
        if len(s) != len(t):
            return False

        hmap = defaultdict(int)
        for char in s:
            hmap[char] += 1
        
        for char in t:
            if char not in hmap or hmap[char] <= 0:
                return False
            hmap[char] -= 1

        return True