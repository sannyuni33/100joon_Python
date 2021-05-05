#You may use import as below.
#import math

def solution(num):
    # Write code here.
    num = str(num + 1)
    answer = ''
    for i in range(len(num)):
        if num[i] == '0':
            answer += '1'
        else:
            answer += num[i]
    print(answer)
    return answer


#The following is code to output testcase.
num = 9949999;
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")


# 일단 1 더하고 0인 애들을 1로 바꿔주는 방식.