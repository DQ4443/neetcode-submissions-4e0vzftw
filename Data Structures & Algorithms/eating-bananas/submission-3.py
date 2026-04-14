class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search speed for lowest value
        # range = [1, max(piles)]
        # if can finish, look for lower speed
        # else look for higher speed
        # need check each value

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            time = 0
            for pile in piles:
                time += -(-pile // mid)

            if time <= h:
                high = mid - 1
            else:
                low = mid + 1
        
        return low