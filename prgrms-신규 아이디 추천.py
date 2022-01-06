def solution(new_id):
    answer = ''
    temp = ''
    #대문자와 허용되지 않는 특수 문자 걸러내는 로직
    for i in range(len(new_id)):
        pt = ord(new_id[i])
        # 대문자인 경우

        if pt < 91 and (64 < pt):
            temp += chr(pt + 32)
        # 소문자, tntwk

        elif (pt > 48 and pt < 58) or (pt > 96 and pt < 123):
            temp += chr(pt)
        # 허용되는 특수문자
        elif pt in [45, 46, 95]:
            temp += chr(pt)

    new_id = temp
    temp = ''
    #중복된 .을 제거하는 로직
    bef = ''
    for i in range(len(new_id)):
        if new_id[i] == '.' and new_id[i] == bef:
            bef = new_id[i]
        else:
            bef = new_id[i]
            temp += new_id[i]
    new_id = temp
    temp = ''
    #맨 앞, 뒤의 .을 제거하는 로직
    while new_id[0] == '.' or new_id[-1] == '.':
        if new_id[0] == '.':
            new_id = new_id[1:]
            if new_id == '':
                break
        elif len(new_id) > 1 and new_id[-1] == '.':
            new_id = new_id[0:-1]
            if new_id == '':
                break

    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id


new_id = "...!@BaT#*..y.abcdefghijklm"

print(solution(new_id))