class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #  longest_prefix = ""
        #  for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return longest_prefix
        #     longest_prefix+=strs[0][i]
        
        #  return longest_prefix

        ref = strs[0]
        for i in range(1,len(strs)):
            cur = strs[i]
            j=0
            while j<len(ref) and j <len(cur) and ref[j] == cur[j]:
                j+=1
            ref = ref[0:j]
        return ref 












