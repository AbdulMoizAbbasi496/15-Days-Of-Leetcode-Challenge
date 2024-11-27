class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            word=haystack[i:i+len(needle)]
            if word==needle:
                return i    

        return -1                         