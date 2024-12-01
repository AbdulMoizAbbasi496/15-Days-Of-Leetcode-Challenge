class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxL = 0

        for i in range(n):
            substring=""
            for j in range(i,n):
                if s[j] in substring:
                    break
                substring+=s[j]          
            l = len(substring)
            if l > maxL:
                maxL = l
        return maxL    
    

