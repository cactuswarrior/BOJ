import sys
sys.stdin = open('9663.txt', 'r')
M = int(input())

board = [0]*(M+1) #1차원배열에 숫자로 열의 위치 입력
# print(board)
cnt = 0
def queen(board, line):
    global cnt
    n = len(board)-1
    if (promising(board, line)):
        if (line == n):
            cnt += 1
            # print(board[1:n+1])
        else:
            for j in range(1, n + 1):
                board[line+1] = j
                queen(board, line + 1)

def promising(board, line):
    k = 1
    flag = True
    while (k < line and flag):
        if (board[line] == board[k]) or abs(board[line] - board[k]) == (line - k):
            flag = False
        k += 1
    return flag

queen(board, 0)
print(cnt)
