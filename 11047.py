import sys
sys.stdin = open('11047.txt', 'r')
N, K = input().split()
N, K = int(N), int(K)
coin = []
for i in range(N):
    coin.append(int(input()))
coin.reverse()

idx = 0
cnt = 0
while K > 0:
    if K >= coin[idx]:
        M = K//coin[idx]
        K %= coin[idx]
        cnt += M
    idx += 1
print(cnt)


