nums = [1, 2, 3, 4, 5, 6, 7, 9]

if len(nums) < 3:
    print("Здається у Вас бракує чисел.. Потрібно щонайменше 3. ;) ")
else:
    result = [nums[0], nums[2], nums[-2]]
    print(result)