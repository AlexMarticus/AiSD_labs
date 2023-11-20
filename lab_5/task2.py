import random


def matrix(dims, i, j):
    if j <= i + 1:  # если одна матрица
        return 0

    min = 10 ** 100  # ищем минимальное количество операций

    for k in range(i + 1, j):

        # повторяется для `M[i+1]…M[k]`, чтобы получить матрицу `i × k`
        cost = matrix(dims, i, k)

        # повторяется для `M[k+1]…M[j]`, чтобы получить матрицу `k × j`
        cost += matrix(dims, k, j)

        # стоимость умножения двух матриц `i × k` и `k × j`
        cost += dims[i] * dims[k] * dims[j]

        if cost < min:
            min = cost

    return min


dims = [random.randint(2, 100) for i in range(15)]
print(dims)  # матрицы размерностью dims[i-1] x dims[i]
print('Минимальное количество операций: ', matrix(dims, 0, len(dims) - 1))
