class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums) 
        vals={}
        for i in range(n):
            if nums[i] not in vals:
                count=0
                for j in range(i,n):
                    if nums[i]==nums[j]:
                        count+=1
                vals[nums[i]]=count
        
        max_key = max(vals, key=vals.get)
        return max_key          

