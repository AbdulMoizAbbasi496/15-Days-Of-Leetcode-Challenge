class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars=list(s)
        for i in range(len(t)):
            if t[i] in s_chars:
                s_chars.remove(t[i])
            else:
                return False    
        return len(s_chars)==0        

