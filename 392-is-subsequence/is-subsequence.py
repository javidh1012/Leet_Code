class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt1,pt2=0,0

        while pt1 < len(s) and pt2 < len(t):
            if s[pt1] == t[pt2]:
                 pt1 +=1
                 pt2 +=1
            else:
                pt2 +=1

        if len(s) == pt1:
            return True
        else:
            return False
        