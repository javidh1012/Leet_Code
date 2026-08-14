class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        most_occurance = {}
        for x in nums:
            if x  in most_occurance:
                most_occurance[x] += 1
            else:
                most_occurance[x] = 1
        return max(most_occurance,key=most_occurance.get)