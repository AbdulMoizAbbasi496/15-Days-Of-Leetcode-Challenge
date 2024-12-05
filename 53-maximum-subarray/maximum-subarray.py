class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=nums[0]
        max_sum=nums[0]
        n=len(nums)
        for i in range(1,n):
            current_sum=max(nums[i],current_sum+nums[i])
            if current_sum>max_sum:
                max_sum=current_sum
        return max_sum        