from random import randint
n = int(input('Введите длину списка, из которого необходимо выбрать наибольшую непрерывную'
              ' возрастающую подпоследовательность: '))
arr = [randint(-100, 100) for i in range(n)]
q = [1]*n
for i in range(1, len(arr)):
    if arr[i]>arr[i-1]: q[i] = q[i-1]+1
print(f'Длина наибольшей непрерывной возрастающей подпоследовательности = {max(q)}')
