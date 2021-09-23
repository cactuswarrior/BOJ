seq = input()
cups = [1, 0, 0, 2]
for i in seq:
    if i == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif i == 'B':
        cups[0], cups[2] = cups[2], cups[0]
    elif i == 'C':
        cups[0], cups[3] = cups[3], cups[0]
    elif i == 'D':
        cups[1], cups[2] = cups[2], cups[1]
    elif i == 'E':
        cups[1], cups[3] = cups[3], cups[1]
    else:
        cups[0], cups[3] = cups[3], cups[0]
print(cups.index(1) + 1)
print(cups.index(2) + 1)