import sys
sys.stdin = open('1541.txt', 'r')

arr = input()
# print(arr)
num = []
for i in range(10):
    num.append(str(i))
# print(num)
temp = ''
sik = []
total = 0
booho = ''
for i in range(len(arr)):
    if arr[i] in num:
        temp += arr[i]
    else:
        sik.append(int(temp))
        sik.append(arr[i])
        temp = ''
    if i == len(arr)-1:
        # print('done')
        sik.append(int(temp))
    # print('temp', temp)
# print(sik)
temp = 0
bra = 0
for i in range(len(sik)):
    if sik[i] != "+" and sik[i] != "-":
        if booho == "" or booho == "+":
            total += sik[i]
        elif booho == "-":
            bra += sik[i]
    elif sik[i] == "-":
        if booho == "-":
            total -= bra
            bra = 0
        elif booho == "+" or booho == "":
            booho = "-"
    else:
        if booho == "-":
            continue
        elif booho == "+" or booho == "":
            total += temp
            temp = 0
    if i == len(sik) -1:
        if bra:
            total -= bra
        elif temp:
            total += temp




print(total)