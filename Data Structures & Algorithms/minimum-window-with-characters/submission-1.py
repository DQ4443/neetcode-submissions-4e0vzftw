class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window, expand, then if satisfies, try shrink
        # use hashmap to store letters needed in t
        # use hashamp to store letters of window
        # use have counter to not have to check all values in hashmap every step
        # when the have map matches the value of the need map, increment
        # needs to match exactly to not double count values over the needed

        if not s or not t:
            return ""
        
        needMap = defaultdict(int)
        for char in t:
            needMap[char] += 1
        
        have = 0
        need = len(needMap) # this many distinct letters (reqs) need to satisfy
        window = defaultdict(int)
        res_len = len(s) + 1
        res = [-1, -1]


        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            # update have if req filled
            if window[char] == needMap[char]:
                have += 1

            # if have == need, update result and attempt shrink window (while)
            while have == need:
                # update result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # shrink window
                window[s[l]] -= 1
                if s[l] in needMap and window[s[l]] < needMap[s[l]]:
                    have -= 1

                l += 1

        a, b = res
        return s[a:b + 1] if res_len <= len(s) else ""

                