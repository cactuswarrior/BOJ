import sys
sys.stdin = open('1018.txt', 'r')
tc = int(input())

for i in range(tc):
    arr = []
    N, M = map(int, input().split())
    for j in range(N):
        arr.append(list(input()))
    res = []

    mini = 1000000
    cnt_1 = 0
    cnt_2 = 0
    for i in range(N-7):
        for j in range(M-7):
                # if i + 7 < N and j + 7 < M:
                for k in range(i, i+8):
                    for l in range(j, j+8):
                        # if i + k < N and j + l < M:
                        if (k + l)%2:
                            if arr[k][l] != 'B':
                                cnt_1 += 1
                        else:
                            if arr[k][l] != 'W':
                                cnt_2 += 1


                        if (k + l)%2:
                            if arr[k][l] != 'W':
                                cnt_2 += 1
                        else:
                            if arr[k][l] != 'B':
                                cnt_1 += 1

                res.append(cnt_1)
                res.append(cnt_2)
                cnt_1 = 0
                cnt_2 = 0
    print(res)

    print(min(res))