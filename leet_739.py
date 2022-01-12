def dailyTemperatures(temperatures):
    answer = []
    for i in range(len(temperatures)):
        day = 1
        if i == len(temperatures)-1:
            answer.append(0)
            break
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] <= temperatures[i]:
                day += 1
            elif temperatures[j] > temperatures[i]:
                answer.append(day)
                break
            if day >= len(range(i+1, len(temperatures))):
                answer.append(0)



    return answer

temperatures = [30,60,90]
print(dailyTemperatures(temperatures))