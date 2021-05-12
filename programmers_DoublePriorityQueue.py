from collections import deque

def solution(operations):
    deq = deque()

    for op in operations:
        x = op.split(' ')

        if x[0] == "I":
            num = int(x[1])
            if not len(deq):
                deq.append(num)
            else:
                if num >= deq[0]:
                    deq.appendleft(num)
                elif num <= deq[-1]:
                    deq.append(num)
        elif x[0] == "D":
            if not len(deq):
                continue
            if x[1] == '1':
                deq.popleft()
            else:
                deq.pop()
    if not len(deq):
        answer = [0, 0]
    else:
        answer = [deq[0], deq[-1]]
    print(answer)
    return answer

# solution(["I 16","D 1"])
# solution(["I 7","I 5","I -5","D -1"])
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])