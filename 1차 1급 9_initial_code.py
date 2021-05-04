def func(record):  # 리턴은 A가 낸거
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution(recordA, recordB):
    cnt = 0  # 현재 위치
    for i in range(len(recordA)):  # 이상무
        if recordA[i] == recordB[i]:
            continue                # 이상무
        elif recordA[i] == func(recordB[i]):  # A가 이김
            cnt = cnt + 3
        elif cnt >= 1:       # A가 짐
            cnt = cnt - 1  # 0 아래로 떨어질 수 있는 부분이 문제
    return cnt

#The following is code to output testcase. The code below is correct and you shall correct solution function.
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]

ret = solution(recordA, recordB)


#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")