class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s, t):
            return sorted(s) == sorted(t)

        res = []
        for word in strs:
            grouped = False
            # check every group to see if it fits anywhere
            for group in res:
                # if fits, add to group
                if is_anagram(group[0], word):
                    group += [word]
                    grouped = True
                    break

            # else, make a new group
            if not grouped:
                res += [[word]]

        print(res)
        return res
            

            