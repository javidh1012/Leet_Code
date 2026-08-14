class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for i in range(len(magazine)):
            if magazine[i] not in hash_map:
                hash_map[magazine[i]] = 1
            else:
                hash_map[magazine[i]] += 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in hash_map and hash_map[ransomNote[i]] != 0:
                hash_map[ransomNote[i]] -=1
            else:
                return False
        return True

            


