a = input()
k = ''

for i in range(len(a) // 2):
    a = a.replace('(' + k + ')', k + '00')
    a = a.replace('[' + k + ']', k + '00')
    a = a.replace('{' + k + '}', k + '00')

    k += '00'

if '(' in a or ')' in a or '[' in a or ']' in a or '{' in a or '}' in a:
    for el in a:
        if el != '0':
            f = a.index(el) + 1
            break
    print(' ' * (f - 1) + '^')
    print("Введенная скобочная структура неправильная. Ошибка на скобке номер " + str(f))

else:
    print("Введенная скобочная структура правильная.")
