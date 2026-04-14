class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on k, eating speed
        # floor is 1, ceiling is max(piles)

        low = 1
        high = max(piles)

        while low <= high: # check all values
            mid = (low + high) // 2

            # if can eat, cut bottom. if not, cut top
            time = 0
            for pile in piles:
                time += -(-pile // mid) # ceil divide

            # can finish
            if time <= h:
                high = mid - 1
            else:
                low = mid + 1

        return low