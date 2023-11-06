def copy_list(list_):
    li = []
    for i1 in list_:
        l1 = []
        for j in i1:
            l1.append(j.copy())
        li.append(l1)
    return li


def find_way(labyrinth_list: [list[int]], now_position: (int, int, int)):
    global MAX_COUNT_LINE, MAX_COUNT_COLUMN, MAX_COUNT_DEPTH
    line_, column_, depth_ = now_position[0], now_position[1], now_position[2]
    labyrinth_list[line_][column_][depth_] = 2
    n1, n2, n3, n4, n5, n6 = None, None, None, None, None, None
    if line_ - 1 > 0:
        if labyrinth_list[line_ - 1][column_][depth_] == 0:
            if line_ - 1 in (0, MAX_COUNT_LINE - 1):
                labyrinth_list[line_ - 1][column_][depth_] = 2
                return labyrinth_list
            else:
                n1 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_ - 1, column_, depth_))
    if line_ + 1 < MAX_COUNT_LINE:
        if labyrinth_list[line_ + 1][column_][depth_] == 0:
            if line_ + 1 in (0, MAX_COUNT_LINE - 1):
                labyrinth_list[line_ + 1][column_][depth_] = 2
                return labyrinth_list
            else:
                n2 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_ + 1, column_, depth_))
    if column_ - 1 > 0:
        if labyrinth_list[line_][column_ - 1][depth_] == 0:
            if column_ - 1 in (0, MAX_COUNT_COLUMN - 1):
                labyrinth_list[line_][column_ - 1][depth_] = 2
                return labyrinth_list
            else:
                n3 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_, column_ - 1, depth_))
    if column_ + 1 < MAX_COUNT_COLUMN:
        if labyrinth_list[line_][column_ + 1][depth_] == 0:
            if column_ + 1 in (0, MAX_COUNT_COLUMN - 1):
                labyrinth_list[line_][column_ + 1][depth_] = 2
                return labyrinth_list
            else:
                n4 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_, column_ + 1, depth_))
    if depth_ - 1 > 0:
        if labyrinth_list[line_][column_][depth_ - 1] == 0:
            if depth_ - 1 in (0, MAX_COUNT_DEPTH - 1):
                labyrinth_list[line_][column_][depth_ - 1] = 2
                return labyrinth_list
            else:
                n5 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_, column_, depth_ - 1))
    if depth_ + 1 < MAX_COUNT_DEPTH:
        if labyrinth_list[line_][column_][depth_ + 1] == 0:
            if depth_ + 1 in (0, MAX_COUNT_DEPTH - 1):
                labyrinth_list[line_][column_][depth_ + 1] = 2
                return labyrinth_list
            else:
                n6 = find_way(labyrinth_list=copy_list(labyrinth_list), now_position=(line_, column_, depth_ + 1))
    for n in (n1, n2, n3, n4, n5, n6):
        if n is not None:
            return n
    return None


if __name__ == '__main__':
    labyrinth = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    ]
    MAX_COUNT_LINE, MAX_COUNT_COLUMN, MAX_COUNT_DEPTH = len(labyrinth), len(labyrinth[0]), len(labyrinth[0][0])
    way = find_way(labyrinth_list=labyrinth, now_position=(0, 1, 1))
    for i in way:
        print(i)
