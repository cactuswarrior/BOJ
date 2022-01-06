def solution(numbers):
    answer = -1
    res = 0
    numbers.sort()
    realNum = list(range(1, 11))
    for i in range(len(numbers)):
        if numbers[i] in realNum:
            res += numbers[i]
    if res > 0:
        answer = 45-res
    return answer, res



numbers = [1,2,3,4,6,7,8,0]

print(solution(numbers))
