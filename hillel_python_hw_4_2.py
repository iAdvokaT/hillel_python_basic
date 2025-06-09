nums = [1, 3, 5]

if not nums:
    result = 0
else:
    eny_sum = 0
    for i in range(0, len(nums), 2):  # проходимо по 0, 2, 4, ...
        eny_sum += nums[i]
    result = eny_sum * nums[-1]

print(result)