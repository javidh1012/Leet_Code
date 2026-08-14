class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        s = s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i] !=" ":
                k+=1
            else:
                break
        return k

        