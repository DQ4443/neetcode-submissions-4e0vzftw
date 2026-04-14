class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # using division
        num_0 = nums.count(0)

        product_no_zero = 1
        for num in nums:
            if num != 0:
                product_no_zero *= num

        if num_0 == 0:
            return [product_no_zero // num for num in nums]

        if num_0 > 1:
            return [0 for num in nums]

        else:
            return [0 if num != 0 else product_no_zero for num in nums]