from random import randint, choice
import math


firstList = [i for i in range(0, randint(1, 1000))]
secondList = [randint(1, 1000) for _ in range(randint(50, 1000))]

"""
Сложность O(3n):
Есть список целых отсортированных чисел от 0 до N. Нужно вывести
все числа на экран списка [0, 3 * N - 1]
"""
for i in range(0, len(firstList) * 3):
    print(i)

"""
Сложность O(nlogn): (алгоритм quicksort)
Есть неотсортированный список. Нужно его отсортировать
"""
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:   
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)


print(quicksort(secondList))

"""
Сложность O(n!):
"""
def f3(n):
    for _ in range(n):
        print(n)
        f3(n-1)


f3(5)

"""
Сложность O(n^3):
"""
def f4(n):
    for i1 in range(n):
        for i2 in range(n):
            for i3 in range(n):
                print(i1, i2, i3)


f4(5)

"""
Сложность O(3*log(n)):
"""
def f5(n):
    for i in range(1, int(math.log2(n)) + 1):
        for j in range(3):
            print(i, j)


f5(16)