import sys
sys.stdin = open('1931.txt', 'r')
N = int(input())
con_list = []
for i in range(N):
    con_s, con_e = input().split()
    con = [int(con_s), int(con_e)]
    con_list.append(con)

print(con_list)