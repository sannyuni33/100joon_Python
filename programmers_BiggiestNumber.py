def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(numbers)))


solution([3, 30, 34, 5, 9])

# 1 부터 1000 까지를 문자열로 만들고 sorting 하면
# 1, 10, 100, 1000, 101, 102, 103, ... 109, 110,

# 이 문제는 람다함수를 이용해서 숫자들을 정렬했다(오픈소스 참고)
# key=lambda x: x*3
# 이 부분이 핵심인데, 숫자하나의 범위가 1000이하니까
# 세 자리 수로 맞춰주기 위해섯 각 숫자를 문자열로 바꾼뒤 세 번 반복한다고 하는데
# 이게 정확히 무슨 의미인지는 잘 모르겠다...