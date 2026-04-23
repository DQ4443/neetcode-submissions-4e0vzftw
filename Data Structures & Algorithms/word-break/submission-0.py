class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down dp
        # state: remaining string
        # choice: remaining - any valid word in word dict
        # base: whole string
        # ans: at the end. remaining string is empty, then True

        memo = {}

        def dp(remaining):
            if remaining == '':
                return True
            if remaining in memo:
                return memo[remaining]

            for word in wordDict:
                if remaining.startswith(word):
                    res = dp(remaining[len(word):])
                    if res == True:
                        return True

            memo[remaining] = False
            return False

        return dp(s)

