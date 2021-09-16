N = int(input())

sss = []
num = 666
##### 첫번째 풀이 방법 시간이 너무 걸
# while len(sss) < 10000:
#     cnt = 0
#     num = str(num)
#     for j in range(len(num)):
#         j = int(j)
#         if j < len(num)-2:
#             if num[j] == '6' and num[j+1] =='6' and num[j+2] == '6':
#                 sss.append(num)
#     num = int(num)
#     num += 1
#
# print(sss[N])

##### 두번쨰 풀이방법 시간이 많이 줄어들었으나 여전히 오래 걸림
cnt = 0
while len(sss) < 10000:
    if '666' in str(num):
        sss.append(num)

        #### 다른 사람보고 바꾼부분 (정렬을 할 필요가 없었음 수를 1씩 늘리면서 검사했으니)
        cnt += 1
        if cnt == N:
            print(num)
            break
    num += 1


# print(sorted(sss))