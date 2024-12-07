class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x%10==x:
            return True

        n=abs(x)
        r=""
        while n>0:
            dig=n%10
            r+=str(dig)
            n//=10
        
        return int(r)==x