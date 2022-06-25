import sys
sys.stdin = open('test.txt', 'r')
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

def bt(depth):
    global total, maximum
    if depth == 11:
        maximum = max(total, maximum)
        return

    for i in range(11):
        if arr[depth][i] != 0 and not visited[i]:
            visited[i] = 1
            position[depth] = i
            total += arr[depth][i]
            bt(depth+1)
            total -= arr[depth][i]
            position[depth] = -1
            visited[i]= 0


bt(0)
print(maximum)