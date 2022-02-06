import sys
sys.stdin = open('1934.txt', 'r')
TC = int(input())
for i in range(TC):
    A, B = input().split()
    A, B = int(A), int(B)
    arr = [A, B]
    arr.sort(reverse=True)
    X, Y = arr[0], arr[1]
    while True:
        if X%Y:
            X, Y = Y, X%Y
        else:
            mi = Y
            break
    # print(mi)
    ma = A*B/mi
    print(int(ma))