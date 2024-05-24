# nums = [1, 3, 5, 6]
nums = [1,3]
target = 3
print(len(nums))

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        if target <= min(nums):
            return 0
        if target > max(nums):
            return len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] < target <= nums[i]:
                return i


print(Solution().searchInsert(nums, target))
