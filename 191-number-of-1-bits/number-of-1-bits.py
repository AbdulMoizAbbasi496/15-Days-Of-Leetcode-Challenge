class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = ""
        while n>0:
            r = n%2
            b+=str(r)
            n//=2
        b+=str(n)
        b = b[::-1]
        count = 0
        for i in b:
            if i=='1':
                count+=1 
        return count