import sys
sys.stdin = open('5086.txt', 'r')
while True:
    A, B = input().split()
    A, B = int(A), int(B)
    if (A, B) == (0, 0):
        break
    if A < B:
        if B%A == 0:
            print('factor')
        else:
            print('neither')
    elif A > B:
        if A%B == 0:
            print('multiple')
        else:
            print('neither')

