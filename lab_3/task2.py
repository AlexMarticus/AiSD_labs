from random import*
def block_sort(nums):
    if len(nums)<2 or min(nums)==max(nums): return nums
    arr = [[], [], [], []]
    for i in nums:
        if 0<=i<25: arr[0].append(i)
        if 25<=i<50: arr[1].append(i)
        if 50 <= i < 75: arr[2].append(i)
        if 75<= i <=100: arr[3].append(i)

    sort_nums = sorted(arr[0])+sorted(arr[1]+sorted(arr[2])+sorted(arr[3]))
    return sort_nums



def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def merge_two_list(a, b):
    c = []
    i = j = 0
    while i<len(a) and j < len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c+=a[i:]
    if j<len(b):
        c+=b[j:]
    return c
def merge_sort(s):
    if len(s)==1:
        return s
    middle = len(s)//2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)


list1 = [randint(1, 100) for i in range(10)]
print("Изначальный список:")
print(*list1)
list2 = block_sort(list1)
print("Список после применения блочной сортироовки:")
print(*list2)
list1 = [randint(1, 100) for i in range(10)]
print("Изначальный список:")
print(*list1)
list2 = heapSort(list1)
print("Список после применения пирамидальной сортироовки:")
print(*list2)
list1 = [randint(1, 100) for i in range(10)]
print("Изначальный список:")
print(*list1)
list2 = merge_sort(list1)
print("Список после применения сортироовки слиянием:")
print(*list2)