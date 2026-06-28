class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # linear search
        # if target not in nums:
        #     return -1

        # for index, num in enumerate(nums):
        #     if num == target:
        #         return index

        # binary search
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
            
            
            # if num == target:
            #     return index
            # else:
            #     return -1


        