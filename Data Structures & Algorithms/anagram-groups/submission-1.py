class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a hashmap, key on compressed letter frequency list
        if not strs:
            return []

        res = defaultdict(list)
        for s in strs:
            wordList = [0] * 26
            for char in s:
                wordList[ord(char) - ord('a')] += 1
            
            res[tuple(wordList)].append(s)

        return list(res.values())