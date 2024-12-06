class Solution:  
    def rob(self, nums: List[int]) -> int:
        def calc_money(nums:List[int]) -> int:
            rob1=0
            rob2=0
            for money in nums:
                temp=max(rob2,rob1+money)
                rob1=rob2
                rob2=temp            
            return rob2  

        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums)    
        rob1=calc_money(nums[:-1])
        rob2=calc_money(nums[1:])
        return rob1 if rob1>rob2 else rob2    
