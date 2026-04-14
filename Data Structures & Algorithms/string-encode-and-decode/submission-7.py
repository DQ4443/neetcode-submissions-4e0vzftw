class Solution:

    def encode(self, strs: List[str]) -> str:
        # try some format like 5^Hello5^World
        res = ''
        for word in strs:
            res += (f'{len(word)}^{word}')

        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            length = ''
            while s[j] != '^':
                length += s[j]
                j += 1

            length = int(length)
            j += 1
            word = ''
            for _ in range(length):
                word += s[j]
                j += 1

            res.append(word)
            i = j
        return res


