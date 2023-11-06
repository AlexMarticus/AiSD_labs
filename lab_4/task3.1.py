def copy_list(list_):
    li = []
    for i1 in list_:
        li.append(i1.copy())
    return li


def find_way(labyrinth_list: [list[int]], now_position: (int, int)):
    global MAX_COUNT_LINE, MAX_COUNT_COLUMN
    line_, column_ = now_position[0], now_position[1]
    labyrinth_list[line_][column_] = 2
    n1, n2, n3, n4 = None, None, None, None
    if line_ - 1 > 0:
        if labyrinth_list[line_ - 1][column_] == 0:
            if line - 1 in (0, MAX_COUNT_LINE - 1):
                labyrinth_list[line_ - 1][column_] = 2
                return labyrinth_list
            else:
                n1 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_ - 1, column_))
    if line_ + 1 < MAX_COUNT_LINE:
        if labyrinth_list[line_ + 1][column_] == 0:
            if line_ + 1 in (0, MAX_COUNT_LINE - 1):
                labyrinth_list[line_ + 1][column_] = 2
                return labyrinth_list
            else:
                n2 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_ + 1, column_))
    if column_ - 1 > 0:
        if labyrinth_list[line_][column_ - 1] == 0:
            if column_ - 1 in (0, MAX_COUNT_COLUMN - 1):
                labyrinth_list[line_][column_ - 1] = 2
                return labyrinth_list
            else:
                n3 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_, column_ - 1))
    if column_ + 1 < MAX_COUNT_COLUMN:
        if labyrinth_list[line_][column_ + 1] == 0:
            if column_ + 1 in (0, MAX_COUNT_COLUMN - 1):
                labyrinth_list[line_][column_ + 1] = 2
                return labyrinth_list
            else:
                n4 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_, column_ + 1))
    for n in (n1, n2, n3, n4):
        if n is not None:
            return n
    return None


if __name__ == '__main__':
    labyrinth = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                 [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                 [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                 [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                 [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                 [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    MAX_COUNT_LINE, MAX_COUNT_COLUMN = len(labyrinth), len(labyrinth[0])
    start_position = (0, 0)
    for line in range(len(labyrinth)):
        for column in range(len(labyrinth[line])):
            if column in (0, MAX_COUNT_COLUMN - 1) or line in (0, MAX_COUNT_LINE - 1):
                if labyrinth[line][column] == 0:
                    start_position = (line, column)
                    break
        else:
            continue
        break
    way = find_way(labyrinth_list=labyrinth, now_position=start_position)
    for i in way:
        print(i)
