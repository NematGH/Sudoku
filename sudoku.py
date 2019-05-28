import timeit
from copy import deepcopy

s = timeit.default_timer()
"""for saving bigSquare for 9*9 sudoku each 3*3 square is bigSquare """
bigSquare = dict()
"""for saving every empty smallSquare in start 9*9 sudoku consist of 81 small square"""
smallSquare = dict()
"""for saving squares with digit"""
fullPoints = []
"""for saving childs of every big square"""
child = dict()
"""for saving childs of every rows """
rowChild = dict()
"""for saving childs of every cols"""
colChild = dict()
"""for saving digit that does not set in the each row"""
rowNeed = dict()
"""for saving digit that does not set in the each column"""
colNeed = dict()
backList = list()
neighbers = dict()

# board = [[[5, 3, 0], [6, 0, 0], [0, 9, 8]],
#          [[0, 7, 0], [1, 9, 5], [0, 0, 0]],
#          [[0, 0, 0], [0, 0, 0], [0, 6, 0]],
#
#          [[8, 0, 0], [4, 0, 0], [7, 0, 0]],
#          [[0, 6, 0], [8, 0, 3], [0, 2, 0]],
#          [[0, 0, 3], [0, 0, 1], [0, 0, 6]],
#
#          [[0, 6, 0], [0, 0, 0], [0, 0, 0]],
#          [[0, 0, 0], [4, 1, 9], [0, 8, 0]],
#          [[8, 2, 0], [0, 0, 5], [0, 7, 9]]]
#
# board = [[[0, 4, 0], [0, 0, 0], [9, 0, 5]],
#          [[2, 0, 1], [0, 0, 0], [0, 0, 0]],
#          [[0, 6, 0], [0, 0, 0], [3, 0, 7]],
#
#          [[0, 0, 0], [5, 0, 7], [0, 1, 0]],
#          [[0, 0, 0], [0, 8, 0], [0, 0, 0]],
#          [[0, 0, 0], [1, 0, 4], [0, 9, 0]],
#
#          [[0, 0, 1], [0, 0, 0], [6, 0, 8]],
#          [[0, 0, 0], [7, 0, 5], [9, 0, 4]],
#          [[6, 0, 0], [0, 0, 0], [5, 0, 3]]]

"""this is hardest Sudoku in the world so far"""
board = [[[8, 0, 0], [0, 0, 3], [0, 7, 0]],
         [[0, 0, 0], [6, 0, 0], [0, 9, 0]],
         [[0, 0, 0], [0, 0, 0], [2, 0, 0]],

         [[0, 5, 0], [0, 0, 0], [0, 0, 0]],
         [[0, 0, 7], [0, 4, 5], [1, 0, 0]],
         [[0, 0, 0], [7, 0, 0], [0, 3, 0]],

         [[0, 0, 1], [0, 0, 8], [0, 9, 0]],
         [[0, 0, 0], [5, 0, 0], [0, 0, 0]],
         [[0, 6, 8], [0, 1, 0], [4, 0, 0]]]
#
# board = [[[1, 0, 0], [0, 3, 0], [0, 0, 9]],
#          [[0, 0, 7], [0, 2, 0], [6, 0, 0]],
#          [[0, 9, 0], [0, 0, 8], [5, 0, 0]],
#
#          [[0, 0, 5], [0, 1, 0], [6, 0, 0]],
#          [[3, 0, 0], [0, 8, 0], [0, 0, 4]],
#          [[9, 0, 0], [0, 0, 2], [0, 0, 0]],
#
#          [[3, 0, 0], [0, 4, 0], [0, 0, 7]],
#          [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
#          [[0, 1, 0], [0, 0, 7], [3, 0, 0]]]


"""set each big Square and rows and columns domains"""
for i in range(len(board)):
    bigSquare[i] = [list(range(1, len(board) + 1)), False]
    rowNeed[i] = list(range(1, len(board) + 1))
    colNeed[i] = list(range(1, len(board) + 1))

count = 0
for i in board:
    for elem in i:
        for x in elem:
            if x is not 0:
                bigSquare[count][0].remove(x)
    count += 1

del count

"""for print the puzzle"""
def printResult(board):
    a = []
    result = []
    init = 0
    end = 3
    for i in range(3):
        for x in range(3):
            for y in range(init, end):
                for value in board[y][x]:
                    a.append(value)

            result.append(deepcopy(a))
            a.clear()
        init += 3
        end += 3
    for i in result:
        print(i)


"""set child of each row, column and big Square"""
def childing(coordinate, bigger):
    if bigger in child.keys():
        child[bigger].append(coordinate)
    else:
        child[bigger] = [coordinate]

    if coordinate[0] in rowChild.keys():
        rowChild[coordinate[0]].append(coordinate)
    else:
        rowChild[coordinate[0]] = [coordinate]

    if coordinate[1] in colChild.keys():
        colChild[coordinate[1]].append(coordinate)
    else:
        colChild[coordinate[1]] = [coordinate]


"""get coordinate in each big square"""
def coordinate(i):
    if i[0] >= 6:
        x = i[0] - 6
    elif i[0] >= 3:
        x = i[0] - 3
    else:
        x = i[0]

    if i[1] >= 6:
        y = i[1] - 6
    elif i[1] >= 3:
        y = i[1] - 3
    else:
        y = i[1]
    return (x, y)


"""set each small squares domain and full points coordinate"""
bigger = 0
x = y = 0

for row in range(len(board)):
    if row in [3, 4, 5]:
        bigger += 3
    if row in [6, 7, 8]:
        bigger += 6
    for col in range(len(board)):
        if col in [3, 6]:
            bigger += 1
        x, y = coordinate((row, col))

        if board[bigger][x][y] is 0:
            smallSquare[(row, col)] = [deepcopy(bigSquare[bigger][0]), bigger, False]
            childing((row, col), bigger)

        else:
            fullPoints.append([(row, col), board[bigger][x][y]])

    bigger = 0

del bigger, i, x, y

for x in list(smallSquare.keys()):
    for i in fullPoints:
        if i[0][0] == x[0] or i[0][1] == x[1]:
            if i[1] in smallSquare[x][0]:
                smallSquare[x][0].remove(i[1])

for i in fullPoints:
    rowNeed[i[0][0]].remove(i[1])
    colNeed[i[0][1]].remove(i[1])

del row, col, x, i, elem

lenOnePoints = []

"""delete selected value from domains"""
def forwardChecking(coordinate, value, bigsquareNumber):
    global lenOnePoints
    bigSquare[bigsquareNumber][0].remove(value)
    rowNeed[coordinate[0]].remove(value)
    colNeed[coordinate[1]].remove(value)

    for x in list(smallSquare.keys()):
        if coordinate[0] == x[0] or coordinate[1] == x[1]:
            if value in smallSquare[x][0]:
                smallSquare[x][0].remove(value)
                if len(smallSquare[x][0]) == 1:
                    lenOnePoints.append(x)

    for x in child[bigsquareNumber]:
        if value in smallSquare[x][0]:
            smallSquare[x][0].remove(value)
            if len(smallSquare[x][0]) == 1:
                lenOnePoints.append(x)
    return len(lenOnePoints)


"""set all small squares that has just one possible value in domain"""
def onePossbleVariable():
    lenFlag = 1
    while lenFlag > 0:
        lenFlag = 0
        for i in smallSquare:
            if len(smallSquare[i][0]) == 1:
                x, y = coordinate(i)

                if i in lenOnePoints:
                    lenOnePoints.remove(i)
                board[smallSquare[i][1]][x][y] = smallSquare[i][0][0]
                fullPoints.append([(i[0], i[1]), smallSquare[i][0][0]])
                lenFlag = forwardChecking(i, smallSquare[i][0][0], smallSquare[i][1])
                smallSquare[i][0] = []
                smallSquare[i][2] = True
                calculateNeighbor(i, smallSquare[i][1])
                if empty():
                    backtracking()

"""least constraining value calculator"""
def leastCV():
    # bigsquare lcv
    availPoints = []
    for i in bigSquare:
        for value in bigSquare[i][0]:
            for x in child[i]:
                if smallSquare[x][0].count(value) == 1:
                    availPoints.append([x, value, smallSquare[x][1]])
            if len(availPoints) == 1:
                row, col = coordinate(availPoints[0][0])
                board[availPoints[0][2]][row][col] = availPoints[0][1]
                fullPoints.append([availPoints[0][0], availPoints[0][1]])
                forwardChecking(availPoints[0][0], availPoints[0][1], availPoints[0][2])
                smallSquare[availPoints[0][0]][0] = []
                smallSquare[availPoints[0][0]][2] = True
                calculateNeighbor(availPoints[0][0], availPoints[0][2])
                if empty():
                    backtracking()
            availPoints.clear()
    # row lcv
    for i in rowNeed:
        for value in rowNeed[i]:
            for x in rowChild[i]:
                if smallSquare[x][0].count(value) == 1:
                    availPoints.append([x, value, smallSquare[x][1]])

            if len(availPoints) == 1:
                row, col = coordinate(availPoints[0][0])
                board[availPoints[0][2]][row][col] = availPoints[0][1]
                fullPoints.append([availPoints[0][0], availPoints[0][1]])
                forwardChecking(availPoints[0][0], availPoints[0][1], availPoints[0][2])
                smallSquare[availPoints[0][0]][0] = []
                smallSquare[availPoints[0][0]][2] = True
                calculateNeighbor(availPoints[0][0], availPoints[0][2])
                if empty():
                    backtracking()
            availPoints.clear()
    # col lcv
    for i in colNeed:
        for value in colNeed[i]:
            for x in colChild[i]:
                if smallSquare[x][0].count(value) == 1:
                    availPoints.append([x, value, smallSquare[x][1]])

            if len(availPoints) == 1:
                row, col = coordinate(availPoints[0][0])
                board[availPoints[0][2]][row][col] = availPoints[0][1]
                fullPoints.append([availPoints[0][0], availPoints[0][1]])
                forwardChecking(availPoints[0][0], availPoints[0][1], availPoints[0][2])
                smallSquare[availPoints[0][0]][0] = []
                smallSquare[availPoints[0][0]][2] = True
                calculateNeighbor(availPoints[0][0], availPoints[0][2])
                if empty():
                    backtracking()
            availPoints.clear()


"""get empty square with more empty neighbor """
def minNeighborPoint():
    min = 100
    point = None
    for i in smallSquare:
        if not smallSquare[i][2]:
            len1 = len(smallSquare[i][0])
            if len1 < min:
                min = len1
                point = i

    for x in smallSquare:
        if len(smallSquare[x][0]) == min:
            if neighbers[x] > neighbers[point]:
                point = x

    return point


"""when doomains is more than one set one value randomly"""
def randomChoose():
    point = minNeighborPoint()
    backList.append([point, smallSquare[point][0][0], deepcopy(board), deepcopy(smallSquare), deepcopy(bigSquare),
                     deepcopy(fullPoints), deepcopy(rowNeed), deepcopy(colNeed), deepcopy(neighbers)])
    row, col = coordinate(point)
    board[smallSquare[point][1]][row][col] = smallSquare[point][0][0]
    fullPoints.append([point, smallSquare[point][0][0]])
    forwardChecking(point, smallSquare[point][0][0], smallSquare[point][1])
    smallSquare[point][0] = []
    smallSquare[point][2] = True
    calculateNeighbor(point, smallSquare[point][1])
    if empty():
        backtracking()


"""if last randomly selected value is wrong delete that and return variables to the before setting that"""
# xxx =0
def backtracking():
    global board, smallSquare, bigSquare, rowNeed, colNeed, fullPoints, xxx, neighbers
    # xxx+=1
    # print(xxx)
    l = backList.pop()
    board = l[2]
    smallSquare = l[3]
    bigSquare = l[4]
    fullPoints = l[5]
    rowNeed = l[6]
    colNeed = l[7]
    neighbers = l[8]
    smallSquare[l[0]][0].remove(l[1])
    if empty():
        backtracking()


"""find the square that has not value to set"""
def empty():
    for i in smallSquare.values():
        if len(i[0]) == 0 and i[2] is False:
            return 1
    return 0


"""calculate neighbor at the first"""
def neighborNumber():
    for i in smallSquare:
        count = len(bigSquare[smallSquare[i][1]][0]) - 1 + len(rowNeed[i[0]]) + len(colNeed[i[1]])

        for x in child[smallSquare[i][1]]:
            if not smallSquare[x][2]:
                if x == i:
                    count -= 2
                elif x[0] == i[0] or x[1] == i[1]:
                    count -= 1

        neighbers[i] = count
        pass


"""update neighbors number after each digit putting"""
def calculateNeighbor(point, bigger):
    for i in neighbers:
        if point[0] == i[0] or point[1] == i[1]:
            neighbers[i] -= 1
    for i in child[bigger]:
        if point[0] != i[0] and point[1] != i[1]:
            neighbers[i] -= 1


print('Initial State:')
printResult(board)

while 1:

    neighborNumber()
    onePossbleVariable()
    if len(fullPoints) == 81:
        e = timeit.default_timer()
        print('solved....!!! in ', e - s, 'second')
        printResult(board)
        break
    leastCV()
    if len(fullPoints) == 81:
        e = timeit.default_timer()
        print('solved....!!! in ', e - s, 'second')
        printResult(board)
        break
    randomChoose()
