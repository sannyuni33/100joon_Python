#다음과 같이 import를 사용할 수 있습니다.
from itertools import combinations as cb

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0
    lst = list(cb(arr, 3))

    for ls in lst:
        if not sum(ls) % K:
            answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")