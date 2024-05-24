# Input:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1, 1, 2]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# digit_index = 0
# count = 0
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j] and nums[i] != '_':
#             nums[j] = '_'
#             count += 1
#
# # for i in range(len(nums)):
#     # if nums[i] == '_':
#
#             # nums[i], nums[j] = nums[j], nums[i]
#
# print(count)
# print(nums)
# # i = 0
# # while i < len(nums):
# #     if nums[i] == nums[i - 1]:


j = 1
for i in range(len(nums) - 1):
    if nums[i + 1] != nums[i]:
        nums[j] = nums[i + 1]
        j += 1
print(j)
