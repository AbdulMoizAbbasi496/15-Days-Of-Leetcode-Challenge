class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s.rstrip()) - 1
        word = ""

        while i >= 0 and s[i] != " ":
            if s[i] != " ":
                word += s[i]
            i -= 1

        return len(word)