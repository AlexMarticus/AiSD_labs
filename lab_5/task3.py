from random import randint
n = int(input('Введите длину списка, из которого необходимо выбрать наибольшую непрерывную'
              ' возрастающую подпоследовательность: '))
arr = [randint(-100, 100) for i in range(n)]
q = [arr[0]]
ms = len(q)
mq = []
for i in arr:
    if q[-1]<i:
        q.append(i)
        if ms<len(q):
            ms = len(q)
            mq = q
    else:
        q = [i]
print(*mq)
