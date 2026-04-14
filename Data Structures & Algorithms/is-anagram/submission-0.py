class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        for letter in s:
            if letter not in freqs:
                freqs[letter] = 1
            else:
                freqs[letter] += 1

        for letter in t:
            if letter not in freqs or freqs[letter] <= 0:
                return False
            else:
                freqs[letter] -= 1
        
        return len(s) == len(t)