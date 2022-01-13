class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        while ops:
            letter = ops.pop(0)
            if letter not in ["C", "D", "+"]:
                record.append(int(letter))
            elif letter == "C":
                record.pop()
            elif letter == "D":
                temp = record.pop()
                new = temp * 2
                record += [temp, new]

            elif letter == "+":
                temp1 = record[-1]
                temp2 = record[-2]
                new = temp1 + temp2
                record.append(new)

        answer = sum(record)
        return answer