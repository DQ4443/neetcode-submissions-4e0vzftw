class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # at every index, iterate through all of the rest
        # backtrack on palindrom find (s[::-1] == s)
        res = []
        
        def backtrack(i, curr):
            if i == len(s):
                res.append(curr[:])
                return 

            if i > len(s):
                return

            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    curr.append(sub)
                    backtrack(j, curr)
                    curr.pop()

        backtrack(0, [])

        return res