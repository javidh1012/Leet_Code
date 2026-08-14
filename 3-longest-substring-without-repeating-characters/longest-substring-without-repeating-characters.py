class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # subsets = []
        # max_length = 0
        # for string in s:
        #     while string in subsets:
        #         subsets.pop(0)
        #     else:
        #         subsets.append(string)
        #         max_length = max(max_length, len(subsets))
        # return max_length
        l = 0 
        char_string = set()
        res = 0 
        for r in range(len(s)):
            while s[r] in char_string:
                char_string.remove(s[l])
                l+=1
            char_string.add(s[r])
            res = max(res,r-l+1) 

        return res

        
            

        