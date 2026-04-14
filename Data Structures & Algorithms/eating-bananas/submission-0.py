class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time taken to eat a pile is ceil(x / k)
        # loop ceil(x / k) on each element to get total time
        # if total time > h, adjust (binary search)

        def total(k):
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)
            return total_time
        
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2

            if total(mid) <= h:
                res = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        return res 
                
                

        
