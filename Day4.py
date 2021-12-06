with open('./res/Day4.txt', 'r') as file:
    data = list(filter(None, (line.rstrip() for line in file)))

calls = data[0].split(',')
calls = list(map(int, calls))
i = 1
boards = []

while i < len(data):
    boards.append(data[i:i+5])
    i+=5
for i, board in enumerate(boards):
    for x, item in enumerate(board):
        boards[i][x] = list(map(int, item.split()))

def replace_x(number, call):
    if number == call:
        return -1
    else:
        return number

def check_numbers(board):
    # tarkistetaan vaaka
    for line in board:
        if sum(line) == -5:
            return board
    # tarkistetaan pysty
    for i in range(len(board[0])):
        summa = 0
        for line in board:
            summa += line[i]
        if summa == -5:
            return board

    return None

def run_numbers(calls, boards):
    for number in calls:
        for i, board in enumerate(boards):
                for x, board in enumerate(board):
                    boards[i][x] = list(map(lambda x: replace_x(x, number), board))
                if check_numbers(boards[i]):
                    return boards[i], number
    return None

def run_numbers_last(calls, boards):
    boards_left = len(boards)
    last_to_win = None
    for number in calls:
        for i, board in enumerate(boards):
            if board:
                for x, board in enumerate(board):
                    boards[i][x] = list(map(lambda x: replace_x(x, number), board))
                if check_numbers(boards[i]):
                    last_to_win = boards[i]
                    boards[i] = None
                    boards_left -= 1
                # return boards[i], number
            if boards_left == 0:
                return last_to_win, number
    return None

winning_board = run_numbers(calls,boards)
sum_unmarked = 0
for i in range(len(winning_board[0])):
    for n in range(len(winning_board[0][0])):
        if winning_board[0][i][n] != -1:
            sum_unmarked += winning_board[0][i][n]
print(sum_unmarked*winning_board[1])

last_board = run_numbers_last(calls, boards)
sum_unmarked = 0
for i in range(len(last_board[0])):
    for n in range(len(last_board[0][0])):
        if last_board[0][i][n] != -1:
            sum_unmarked += last_board[0][i][n]
print(sum_unmarked*last_board[1])