N = int(input())
fn = [1, 2]
i = 2
if N == 1:
    fn = [1, 1]

while i < N:
    if fn[1] > fn[0]:
        while fn[1] != 1 and i < N:

            i += 1
            fn[1] -= 1
            fn[0] += 1
            # print(i, fn)
            if fn[1] == 1 and i < N:
                i += 1
                fn[0] += 1
                # print(i, fn)
                break
    else:
        while fn[0] != 1 and i < N:

            i += 1
            fn[0] -= 1
            fn[1] += 1
            # print(i, fn)
            if fn[0] == 1 and i < N:
                i += 1
                fn[1] += 1
                # print(i, fn)
                break
print('{}/{}'.format(fn[0], fn[1]))
# 시간 초과