import sys
sys.stdin = open('test.txt', 'r')
def bt(depth, total):
    global maximum
    if depth == 11:
        maximum = max(total, maximum)
        return

    for i in range(11):
        if arr[depth][i] != 0 and not visited[i]:
            visited[i] = 1
            position[depth] = i
            bt(depth+1, total + arr[depth][i])
            position[depth] = -1
            visited[i] = 0

TC = int(input())
for _ in range(TC):
    arr = []
    for i in range(11):
        temp = list(map(int, input().split()))
        arr.append(temp)
    # print(arr)
    maximum = 0
    total = 0
    visited = [0]*11
    position = [0]*11
    bt(0, 0)
    print(maximum)



