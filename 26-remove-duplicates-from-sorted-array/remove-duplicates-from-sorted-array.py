class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited=set()
        k=0
        for num in nums:
            if num not in visited:
                visited.add(num)
                nums[k]=num
                k+=1
        return k