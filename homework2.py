############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Zhihe Chen"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import copy
import random


############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp = 0
        for x in range(n ** 2, n ** 2 - n, -1):
            temp += x
        return temp


def num_placements_one_per_row(n):
    if n == 0: return 0
    return n ** n


# n_queens_valid([0, 0])


# n_queens_valid([0, 3, 1])
def row_valid(borad):
    row = len(borad)
    for x in range(row):

        if sum(borad[x]) > 1: return False
    else:
        return True


def column_valid(borad):
    row = len(borad)
    for x in range(row):
        temp = 0
        for row_list in borad:
            temp += row_list[x]
        if temp > 1: return False
    return True


def diag_(board):
    row = len(board)
    for x in range(2 * row - 1):
        temp = 0
        for y in range(x + 1):
            if 0 <= x - y < row and 0 <= y < row:
                temp += board[y][x - y]
        if temp > 1: return False
    return True


def diag_valid(board):
    return diag_(board) and diag_(tranpose(board))


def tranpose(board):
    row, column = len(board), len(board[0])
    newboard = [[0 for a in range(row)] for b in range(column)]
    for x in range(row):
        for y in range(column):
            newboard[row - 1 - y][x] = board[x][y]
    return newboard


def make_board(row):
    fullboard = [[0 for x in range(row)] for x in range(row)]
    return fullboard


def n_queens_valid(board, length=0):
    row = max(max(board) + 1, len(board), length)
    fullboard = make_board(row)
    for pos, val in enumerate(board):
        fullboard[pos][val] = 1
    return diag_valid(fullboard) and row_valid(fullboard) and column_valid(fullboard)


def n_queens_solutions(n):
    res = []
    alist = [[[], list(range(n))]]
    while alist != []:
        temp = alist.pop()

        for x in temp[1]:
            new_temp1 = temp[0][:]
            new_temp1.append(x)
            new_temp2 = temp[1][:]
            new_temp2.remove(x)

            if helper(new_temp1, new_temp2):
                if len(new_temp1) == n:
                    yield (new_temp1)
                else:
                    alist.append([new_temp1, new_temp2])


def helper(alist, blist):
    total_len = len(alist) + len(blist)

    return n_queens_valid(alist, length=total_len)

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        self.board = [list(x) for x in board]
        self.row = len(self.board)
        self.column = len(self.board[0])

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        self.board[row][col] = not self.board[row][col]
        if row > 0: self.board[row - 1][col] = not self.board[row - 1][col]
        if col > 0: self.board[row][col - 1] = not self.board[row][col - 1]
        if row < self.row - 1: self.board[row + 1][col] = not self.board[row + 1][col]
        if col < self.column - 1: self.board[row][col + 1] = not self.board[row][col + 1]

    def scramble(self):
        for x in range(self.row):
            for y in range(self.column):
                if random.random() < 0.5:
                    self.perform_move(x, y)

    def is_solved(self):
        for x in self.board:
            for y in x:
                if y == True: return False
        return True

    def copy(self):

        return LightsOutPuzzle(self.board)

    def successors(self):
        for x in range(self.row):

            for y in range(self.column):
                temp = self.copy()
                temp.perform_move(x, y)
                yield ((x, y), temp)

    def find_on(self):
        temp = []
        for x in range(self.row):
            for y in range(self.column):
                if self.board[x][y] is True:
                    temp.append([x, y])
        return temp

    def check_around(self, row, col):
        res = []
        if row > 0 and self.board[row - 1][col]:
            res.append([row - 1, col])
        if col > 0 and self.board[row][col - 1]:
            res.append([row, col - 1])
        if row < self.row - 1 and self.board[row + 1][col]:
            res.append([row + 1, col])
        if col < self.column - 1 and self.board[row][col + 1]:
            res.append([row, col + 1])
        return res

    def makefulltuple(self):
        res = []
        for x in range(self.row):
            for y in range(self.column):
                res.append([x, y])
        return res

    def imsuccessors(self, row=-1, col=-1):
        if row == -1 and col == -1:
            for x in range(self.row):
                for y in range(self.column):
                    temp = self.copy()
                    temp.perform_move(x, y)
                    yield ((x, y), temp)
        else:
            for x in range(row, self.row):
                for y in range(self.column):
                    if x != row or y > col:
                        temp = self.copy()
                        temp.perform_move(x, y)
                        yield ((x, y), temp)

    def find_solution(self):
        res = []
        wholemap = [[self.copy(), []]]
        while wholemap:
            temp = wholemap.pop(0)
            x, z = temp[0], temp[1]
            if z:
                succ = list(x.imsuccessors(z[-1][0], z[-1][1]))
            else:
                succ = list(x.imsuccessors())
            if len(succ) >= 1:
                for pos, board in succ:
                    pos = list(pos)

                    if board.is_solved():
                        z.append(pos)
                        return z

                    newstep = z[:]
                    newstep.append(pos)
                    wholemap.append([board, newstep])

        return None


def create_puzzle(rows, cols):
    board = ([[False for x in range(cols)] for y in range(rows)])

    return (LightsOutPuzzle(board))

############################################################
# Section 3: Linear Disk Movement
############################################################

import copy


class Node:
    def __init__(self, number=None, val=None):
        self.number = number
        self.val = None
        self.next = None
        self.pre = None


class lineardisk:
    def __init__(self, length, n):
        self.head = None
        self.tail = None
        self.length = length
        self.n = n

        for x, y in map(None, range(0, self.length, 1), range(0, self.n, 1)):
            self.insert(x, y)
        self.tail = self.search(self.length - 1)

    def insert(self, newdata, value=None):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            self.head.val = value
            return
        lastnode = self.head
        while (lastnode.next):
            lastnode = lastnode.next
        lastnode.next = newnode
        newnode.pre = lastnode
        newnode.val = value

    def listprint(self):
        printval = self.head
        while printval is not None:
            print("this node number", printval.number)
            print("this node value", printval.val)
            if printval.next is not None: print("next node :", printval.next.number)
            if printval.pre is not None: print("previous node :", printval.pre.number)
            printval = printval.next

    def search(self, number=None, value=None):
        findnode = self.head
        if number is not None:
            while findnode.number != number:
                findnode = findnode.next
            return findnode
        elif value is not None:
            while findnode.val != value:
                findnode = findnode.next
            return findnode

    def movenext(self, number):
        temp = copy.deepcopy(self)
        point = temp.search(number)

        point.val, point.next.val = None, point.val
        return temp

    def moveafternext(self, number):
        temp = copy.deepcopy(self)
        point = temp.search(number)

        point.val, point.next.next.val = None, point.val
        return temp

    def movepre(self, number):
        temp = copy.deepcopy(self)
        point = temp.search(number)

        point.val, point.pre.val = None, point.val
        return temp

    def movebepre(self, number):
        temp = copy.deepcopy(self)
        point = temp.search(number)

        point.val, point.pre.pre.val = None, point.val
        return temp

    def justice(self, findnode, number_=None, value_=None):
        # if number_ is not None:findnode=self.search(number=number_)
        # elif value_ is not None: findnode=self.search(value=value_)

        # [can move to right,right right,left,left left]
        res = [False for x in range(4)]

        if findnode.next is not None and findnode.next.val is None:
            res[0] = True
        if findnode.next is not None and findnode.next.next is not None and findnode.next.next.val is None and findnode.next.val is not None:
            res[1] = True
        if findnode.pre is not None and findnode.pre.val is None:
            res[2] = True
        if findnode.pre is not None and findnode.pre.pre is not None and findnode.pre.pre.val is None and findnode.pre.val is not None:
            res[3] = True
        return res

    def checkfinal(self):
        findnode = self.tail
        times = 0

        while times < self.n:
            if findnode.val is not None:
                times += 1
                findnode = findnode.pre
            else:
                return False

        return True

    def ordercheckfinal(self):
        findnode = self.tail
        times = 0

        for x in range(self.n):

            if findnode.val is not None and findnode.val == x:

                findnode = findnode.pre
            else:
                return False

        return True

    def find_valuetail(self):
        findnode = self.tail
        while findnode.val is None:
            findnode = findnode.pre
        return findnode

    def find_valuehead(self):
        findnode = self.head
        while findnode.val is None:
            findnode = findnode.next
        return findnode

    def even(self):
        temp = []

        while not self.checkfinal():
            findnode = self.find_valuetail()
            for time in range(self.n / 2):
                findnode = findnode.pre
                findnode.val, findnode.next.next.val = None, findnode.val
                temp.append([findnode.number, findnode.next.next.number])
                findnode = findnode.pre
        return temp

    def odd(self):
        temp = []
        while not self.checkfinal():
            findnode = self.find_valuetail()
            for time in range(self.n // 2):
                findnode = findnode.pre
                findnode.val, findnode.next.next.val = None, findnode.val
                temp.append([findnode.number, findnode.next.next.number])
                findnode = findnode.pre
            findnodehead = self.find_valuehead()

            findnodehead.val, findnodehead.next.val = None, findnodehead.val
            temp.append([findnodehead.number, findnodehead.next.number])

        return temp

    def helper(self, x):
        if x == 0:
            return 2
        elif x == 1:
            return 3
        elif x == 2:
            return 0
        else:
            return 1

    def successor(self, popvalue):
        node = popvalue[0].head
        alist = []
        last_pos, movement = popvalue[1], popvalue[2]

        last = popvalue[0].helper(last_pos[1])
        for x in range(popvalue[0].length):
            if node.val is not None:
                temp = popvalue[0].justice(node)
                for y in range(4):
                    if x == last_pos[0] and y == last: continue
                    if temp[y] and y == 0:
                        newboard = popvalue[0].movenext(x)

                        pp = copy.deepcopy(popvalue[2])
                        pp.append((x, x + 1))
                        if newboard.ordercheckfinal(): return [True, pp]
                        alist.append([newboard, [x + 1, y], pp])
                    if temp[y] and y == 1:
                        newboard = popvalue[0].moveafternext(x)
                        pp = copy.deepcopy(popvalue[2])
                        pp.append((x, x + 2))
                        if newboard.ordercheckfinal(): return [True, pp]
                        alist.append([newboard, [x + 2, y], pp])
                    if temp[y] and y == 2:
                        newboard = popvalue[0].movepre(x)
                        pp = copy.deepcopy(popvalue[2])
                        pp.append((x, x - 1))

                        if newboard.ordercheckfinal(): return [True, pp]
                        alist.append([newboard, [x - 1, y], pp])
                    if temp[y] and y == 3:
                        newboard = popvalue[0].movebepre(x)
                        pp = copy.deepcopy(popvalue[2])
                        pp.append((x, x - 2))

                        if newboard.ordercheckfinal(): return [True, pp]
                        alist.append([newboard, [x - 2, y], pp])
            node = node.next
        return alist


def solve_identical_disks(length, n):
    disk = lineardisk(length, n)
    if n % 2 == 0:
        return disk.even()
    else:
        return disk.odd()


def solve_distinct_disks(length, n):
    disk = lineardisk(length, n)
    alist = [[disk, [None, None], []]]
    while alist:

        temp = alist.pop(0)

        new_list = disk.successor(temp)
        if new_list[0] is True:
            return new_list[1]

        alist += (new_list)


############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
8 hours
"""

feedback_question_2 = """
time complexity, as the size increase, it costs more time
"""

feedback_question_3 = """
i like the problmes, they are so interesting, like a game
Nope
"""


