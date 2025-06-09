nums = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
i = 0
for num in nums:
    if num != 0:
        nums[i] = num
        i += 1
while i < len(nums):
    nums[i] = 0
    i += 1
print(nums)