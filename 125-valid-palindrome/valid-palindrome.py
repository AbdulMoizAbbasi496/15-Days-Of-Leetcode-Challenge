class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev_str=""
        orig_str=""
        i=0
        while i<len(s):
            if s[i].isalnum():
                orig_str+=s[i]
            i+=1
        j=len(orig_str) - 1            
        while j>=0:
            rev_str+=orig_str[j]
            j-=1
        return rev_str.lower() == orig_str.lower()