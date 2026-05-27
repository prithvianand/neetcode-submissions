class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash_map = {}
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return False
        hash_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in hash_map:
                return [hash_map[diff],i]
            
            hash_map[n] = i
            
        