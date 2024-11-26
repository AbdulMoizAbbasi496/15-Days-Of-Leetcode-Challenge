class Solution:
    def revChunk(self,str:str)->str:
        rev=""
        for i in range(len(str)-1,-1,-1):
            rev+=str[i]
        return rev    
    def reverseStr(self, s: str, k: int) -> str:
        rev=""
        for i in range(0,len(s),2*k):
            t=self.revChunk(s[i:i+k])
            rev+=t
            rev+=s[i+k:i+2*k]
        return rev    
