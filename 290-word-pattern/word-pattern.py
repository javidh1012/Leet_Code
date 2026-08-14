class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_hashmap,string_hashmap = {} ,{}
        if len(pattern) != len(s.split()):
            return False
        for i,j in zip(pattern,s.split()):
            if i in pattern_hashmap and pattern_hashmap[i] != j or j in string_hashmap and string_hashmap[j] !=i:
                return False


            pattern_hashmap[i] = j
            string_hashmap[j] = i
        return True
        
