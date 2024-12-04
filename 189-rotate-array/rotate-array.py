class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        n1=[nums[i] for i in range(n-k,n) ]
        n2=[nums[i] for i in range(n-k) ]
        nums[:]=n1+n2
