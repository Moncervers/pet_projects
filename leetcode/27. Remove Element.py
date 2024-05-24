nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

i = 0
while i < len(nums):
    if val == nums[i]:
        nums.pop(i)
    else:
        i += 1

print(nums)



