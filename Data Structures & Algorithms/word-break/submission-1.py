class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # top down dp
        # state: remaining str
        # choice: for each word in worddict, try remaining - word if valid (startswith)
        # base: whole string
        # ans: return result of starting

        memo = {}

        def dp(remaining):
            if remaining == "":
                return True

            if remaining in memo:
                return memo[remaining]

            for word in wordDict:
                if remaining.startswith(word):
                    if dp(remaining[len(word):]):
                        return True

            memo[remaining] = False
            return False

        return dp(s)