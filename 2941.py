string = input()
cnt = 0
for i in range(len(string)):
    cnt += 1
    if string[i] == '=' and i >= 1:
        if string[i-1] == 'c' or string[i-1] == 's':
            cnt -= 1
            # print(1)
        elif string[i-1] == 'z':
            if string[i-2] == 'd':
                cnt -= 2
                # print(2)
            else:
                cnt -= 1
                # print(3)
    elif string[i] == '-' and i >= 1:
        if string[i-1] == 'd' or string[i-1] == 'c':
            cnt -= 1
            # print(4)
    elif string[i] == 'j' and i >= 1:
        if string[i-1] == 'l' or string[i-1] == 'n':
            cnt -= 1
            # print(5)
print(cnt)

