from random import randint
array=[randint(1, 10000) for i in range(100)]
print(f'Список до пузырьковой сортировки:{array}')
for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j]>array[j+1]:
            temporary=array[j]
            array[j]=array[j+1]
            array[j+1]=temporary

print(f'Список после пузырьковой сортировки:{array}')
