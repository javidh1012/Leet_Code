class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash_map = {}
        for i,val in enumerate(nums):
            if val in hash_map and (i - hash_map[val])<=k:
                return True
            else:
                hash_map[val] = i
        return False

