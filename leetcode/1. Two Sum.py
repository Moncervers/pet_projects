num = [2, 7, 11, 15]
target = 9

# 1718 ms
for i in range(len(num)):
    for j in range(len(num)):
        if i + j == target:
            print(num[i], num[j])
print()

# 108 ms
# todo debug and find out why so fast
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     for i in range(len(nums) - 1, -1, -1):
#         j = target - nums[i]
#         if (j in nums and nums.index(j) != i):
#             return [i, nums.index(j)]
# temp
