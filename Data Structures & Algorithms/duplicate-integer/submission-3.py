class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_mapping = []
        for i in nums:
            if i not in count_mapping:
                count_mapping.append(i)
            else:
                return True
        return False
        