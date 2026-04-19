class Solution:
    def longestPalindrome(self, s: str) -> str:
        # use two pointer approach, start from inside out
        if len(s) < 2:
            return s

        res = ''

        def check(l, r):
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1

        for i in range(len(s) - 1):
            check(i, i)
            check(i, i + 1)

        return res