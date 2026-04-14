class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        have = 0
        need_total = len(need)

        res = [-1, -1]

        res_len = (float('inf'))

        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # che k if char now satifies a req:
            if char in need and window[char] == need[char]:
                have += 1

            # try shrink window
            while have >= need_total:
                # update result
                if (right - left + 1) < res_len: # shorter
                    res = [left, right]
                    res_len = right - left + 1

                # remove left character
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left += 1

        left, right = res
        return s[left : right + 1] if res_len != float('-inf') else ""