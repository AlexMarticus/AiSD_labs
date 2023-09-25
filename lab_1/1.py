step = 0
left = 0
nums = [i for i in range (1,100001)]
task = int(input("Введите число от 1 до 100000, которое необходимо найти:"))
right = len (nums)
mid = 0

while left + 1 < right:
    step += 1
    mid  = (left + right) // 2
    if nums[mid]==task:
        break
    if nums [mid] < task:
        left = mid + 1
    else:
        right = mid - 1 
print(f"Шагов потребуется: {step}, чтобы найти число {task}, с помощью бинарного поиска.")
