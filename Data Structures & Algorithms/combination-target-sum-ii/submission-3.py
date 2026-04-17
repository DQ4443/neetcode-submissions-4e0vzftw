class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # append case if amount left == 0
        # exit case if amount left < 0, i > len(candidates)
        # carry a set for seen

        res = []
        candidates.sort()

        def backtrack(i, curr, left):
            if left == 0 and curr not in res:
                res.append(curr[:])
                return

            if i >= len(candidates) or left < 0:
                return 

            # include
            backtrack(i + 1, curr + [candidates[i]], left - candidates[i])

            # skip duplicate candidates
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
        
            backtrack(i + 1, curr, left)

        backtrack(0, [], target)

        return res