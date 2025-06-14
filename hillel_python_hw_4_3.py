# nums = [1, 2, 3, 4, 5, 6, 7, 9]
#
# if len(nums) < 3:
#     print("Здається у Вас бракує чисел.. Потрібно щонайменше 3. ;) ")
# else:
#     result = [nums[0], nums[2], nums[-2]]
#     print(result)

#v2

import random

length = random.randint(3, 10)
nums = [random.randint(1, 20) for _ in range(length)]

result = [nums[0], nums[2], nums[-2]]

print("Початковий список:", nums)
print("Результат:", result)