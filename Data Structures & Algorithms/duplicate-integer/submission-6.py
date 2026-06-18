class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count_mapping = []
        # for i in nums:
        #     if i not in count_mapping:
        #         count_mapping.append(i)
        #     else:
        #         return True
        # return False
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        # return len(nums) != len(set(nums))

        