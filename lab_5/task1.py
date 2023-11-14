from random import randint
l = int(input('Введите количество экспонатов: '))
n = int(input('Введите количество заходов вора: '))
k = int(input('Введите максимальный вес, который может забрать с собой вор: '))
arr = [[randint(0, 1000000), randint(1, k)] for i in range(l)]
rob = []

for i in range(n):
    r = 0
    new_arr = []
    for j in sorted(arr, key=lambda x:[-x[0], x[1]]):
        if r+j[1]<k:
            r+=j[1]
            rob+=[j]
        else:
            new_arr.append(j)
    arr = new_arr
rs=sum(s[0] for s in rob)
print(f'Максимальная украденная сумма = {rs}')
print('Вор унес следующие экспонаты:')
for j in rob:
    print(*j)
