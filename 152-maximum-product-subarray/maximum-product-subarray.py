class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_till_now = nums[0]
        min_till_now = nums[0]
        product = nums[0]    

        for i in range(1, len(nums)):
            curr = nums[i]
            
            if curr < 0:
                max_till_now, min_till_now = min_till_now, max_till_now
            
            max_till_now = max(curr, max_till_now * curr)
            min_till_now = min(curr, min_till_now * curr)
            
            product = max(product, max_till_now)
        
        return product