class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        n=len(s)
        word=""
        words=[]
        for i in range(n):
            if s[i].isalpha() or s[i].isdigit():
                word+=s[i]
            elif s[i]==' ':
                if word:
                    words.append(word)
                    word=""   
        if word:
                words.append(word)
        res=""                
        for i in range(len(words)-1,-1,-1):
            res+=words[i]+" "
        return res.strip()  
