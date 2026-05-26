class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen_hash_mapping = {}
      for ind, num in enumerate(nums):

         diff = target - num

         if diff in seen_hash_mapping:
            return [seen_hash_mapping[diff], ind]
         seen_hash_mapping[num] = ind
         
         
