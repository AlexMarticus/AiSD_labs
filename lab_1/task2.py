students = {}
with open('opros_k3123.txt', encoding='utf-8') as g:
    questions = list(g.readline().split(','))
    spisok = (g.readlines())
    questions[-1]=questions[-1][:-1]
    for man in spisok:
        parametr = man.split(',')
        if '\n' in parametr[-1]:parametr[-1]=parametr[-1][:-1]
        students[parametr[1]]=parametr[2:]
user_answer = list()
list_before = list(students.keys())
list_after = list()
def search():
    for man in list_before:
        if user_answer == students[man][:len(user_answer)]:
            list_after.append(man)

print('Загадайте студента из группы К3123 и ответьте на следующие вопросы.')
for num in range(1, len(questions)):
    answer = input(questions[num])
    while answer != 'да' and answer != 'нет':
        answer = input(f'Ответ введен некорректно, ответьте на вопрос "{questions[num]}" заново "да" или "нет".')
    user_answer.append(answer)
    search()
    if len(list_after)==1:
        print(*list_after)
        break
    if len(list_after)==0:
        print('Студента с заданными параметрами нет в группе К3123.')
        break
    list_before = list_after
    list_after = []