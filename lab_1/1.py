from random import randint
step = 0
left = 0
nums = sorted([randint(1,5000) for i in range(3000)])
task = int(input("Введите число, которое необходимо найти:"))
right = len (nums)
mid = 0
while left + 1 < right:
    step += 1
    mid  = (left + right) // 2
    if nums [mid] < task:
        left = mid
    else:
        right = mid
print(f"Шагов потребуется: {step}")
