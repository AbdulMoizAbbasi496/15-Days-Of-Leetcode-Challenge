class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest = strs[0]
        for string in strs:
            if len(string) < len(shortest):
                shortest = string
        
        prefix = shortest
        
        for i in range(len(prefix)):
            for string in strs:
                if string[i] != prefix[i]:
                    return prefix[:i]
        
        return prefix  
