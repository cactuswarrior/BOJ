import sys
sys.stdin = open('2675.txt', "r")

TC = int(input())
# print(TC)
for _ in range(TC):
    N, word = input().split(' ')
    # print(N, word)

    for i in word:
        # print(i)
        for _ in range(int(N)):
            print(i,  end='')
    print()
