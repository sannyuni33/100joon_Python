# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(s1, s2):
    # 여기에 코드를 작성해주세요.
    global flag
    answer = 0
    for i in range(len(s1)):
        if s2[0] == s1[i]:  # 겹치는 부분 발견
            print(i, '번째서 탐색시작')
            for j in range(i, min(len(s1), len(s2))-i):
                flag = 0
                if s1[i+j] != s2[flag]:
                    flag = -1
                    break
                else:
                    flag += 1
        if flag != -1:
            new1 = s1 + s2[flag:]
            print(new1)
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
