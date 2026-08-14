class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)-1):
        #     for j in range(1,len(nums)):
        #         if (nums[i]+nums[j]) == target:
        #             return [i,j]
        #             break
        #     return [-1,-1]
        
        hash_map = {}
        for current_pointer in range(len(nums)):
            x = target - nums[current_pointer]
            if x in hash_map:
                return [hash_map[x],current_pointer]
                break
            hash_map[nums[current_pointer]] = current_pointer
        return [-1,-1]


        # hash_map = {}

        # for i in range(len(nums)):   
        #     x = target - nums[i]  
        #     if x in hash_map:  
        #         return hash_map[x],i
        #         break
        #     hash_map[nums[i]] = i 
        # return None

        



        


        