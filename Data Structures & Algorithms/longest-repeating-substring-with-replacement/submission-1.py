class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # slide a window over to get the max length
        # use hashmap to store frequency
        # keep track of the most frequent element with a variable. update if more frequent one appears
        # updates needed = len(window) - hashmap[freq_letter]
        # update right pointer until updates needed > k
        # update left pointer until updates needed < k again
        # calculate the max length at each window expansion

        freq = {}
        most_freq = 0
        max_L = 0

        l, r = 0, 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            most_freq = max(most_freq, freq[s[r]])

            while r - l + 1 - most_freq > k:
                freq[s[l]] -= 1
                l += 1

            max_L = max(max_L, r - l + 1)
            r += 1

        return max_L
            
                