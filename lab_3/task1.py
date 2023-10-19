import timeit
from random import *
import random
def quicksort(num):
    if len(num)<=1:return num
    q = random.choice(num)
    s_nums = []
    m_nums = []
    e_nums = []
    for n in num:
        if n < q: s_nums.append(n)
        elif n > q: m_nums.append(n)
        else: e_nums.append(n)
    return quicksort(s_nums)+e_nums+quicksort(m_nums)

def comb_sort(nums):
    k = len(nums)
    while k>0:
        if k<1:
            k = 1
        else:k = int(k/1.247)
        for i in range(len(nums)-k):
            if nums[i]>nums[i+k]:
                nums[i], nums[i+k] = nums[i+k], nums[i]
        if k==1:
            break
    return nums
list1 = [randint(1, 100) for i in range(15)]
print('Изначальный список')
print(*list1)
list2 = quicksort(list1)
print('Список, прошедший через быструю сортировку')
print(*list2)
list3 = comb_sort(list1)
print('Список, прошедший через сортировку расческой')
print(*list3)
code = '''
def quicksort(num):
    if len(num)<=1:return num
    q = random.choice(num)
    s_nums = []
    m_nums = []
    e_nums = []
    for n in num:
        if n < q: s_nums.append(n)
        elif n > q: m_nums.append(n)
        else: e_nums.append(n)
    return quicksort(s_nums)+e_nums+quicksort(m_nums)
'''
print(f'Время работы быстрой сортировки = {timeit.timeit(code, setup=code, number=1000)}')
code = '''
def comb_sort(nums):
    k = len(nums)
    sorted = False
    while not sorted:
        if k<1:
            k = 1
        else:k = int(k/1.247)
        sorted = True
        for i in range(len(nums)-k):
            if nums[i]>nums[i+k]:
                nums[i], nums[i+k] = nums[i+k], nums[i]
                sorted = False
    return nums
'''

print(f'Время работы сортировки расческой = {timeit.timeit(code, setup=code, number=1000)}')
