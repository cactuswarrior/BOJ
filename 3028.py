seq = input()
cups = [1, 0, 0]
for i in seq:
    if i == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif i == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    else:
        cups[0], cups[2] = cups[2], cups[0]
print(cups.index(1) + 1)