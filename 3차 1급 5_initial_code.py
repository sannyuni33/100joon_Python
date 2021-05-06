# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    # 여기에 코드를 작성해주세요.
    answer = ''
    blank = '--------------'

    if not (second//14) % 2:  # 공백이 먼저
        answer += blank[second % 14:]
        answer += phrases[:second % 14]
    else:  # 문구가 먼저
        answer += phrases[second % 14:]
        answer += blank[:second % 14]

    print(answer)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "happy-birthday"
second = 29
ret = solution(phrases, second)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")