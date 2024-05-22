nums = [1, 2, 3, 4]

output = [0] * len(nums)
output[0] = nums[0]
for i in range(1, len(nums)):
    output[i] = output[i - 1] + nums[i]

print(output)
