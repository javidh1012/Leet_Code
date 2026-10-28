class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) !=len(t):
        #     return False
        # hash_map = {}

        # for i in range(len(s)):
        #     if s[i] not in hash_map:
        #         hash_map[s[i]] = 1
        #     else:
        #         hash_map[s[i]] += 1
        
        # for i in range(len(t)):
        #     if t[i] in hash_map and hash_map[t[i]]!=0:
        #         hash_map[t[i]] -=1
        #     else:
        #         return False
        # return True

        s_f , t_f = {} , {} 
        if len(s) != len(t):
            return False
        for char in s:
            s_f[char] = s_f.get(char,0)+1
        for char in t:
            t_f[char] = t_f.get(char,0)+1
        return s_f == t_f




    
        