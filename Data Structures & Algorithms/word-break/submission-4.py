class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down dp, use memo
        # state: remiainig string
        # choice: for every word in wordDict, if remaining starts with word, can you cut off and recurse
        # base: full string s
        # ans: recurse on the base case
        # direction: left to right
        memo = {}

        def dp(remaining):
            if remaining == "":
                return True

            if remaining in memo:
                return memo[remaining]

            for word in wordDict:
                if remaining.startswith(word):
                    result = dp(remaining[len(word):])
                    print(remaining)
                    if result:
                        return True

            memo[remaining] = False
            return False

        return dp(s)
