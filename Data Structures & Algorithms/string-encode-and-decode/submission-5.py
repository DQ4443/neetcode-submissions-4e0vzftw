class Solution:
    def __init__(self):
        self.spacings = []


    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += word
            self.spacings += [len(word)]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        for num in self.spacings:
            word = s[:num]
            res += [word]
            s = s[num:]

        return res
