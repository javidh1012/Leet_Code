class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in range(len(haystack) - len(needle) + 1):
        #     matches = True
        #     for j in range(len(needle)):
        #         if haystack[i+j] != needle[j]:
        #             matches = False
        #             break
        #     if matches:
        #         return i
        # return -1


        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
   

