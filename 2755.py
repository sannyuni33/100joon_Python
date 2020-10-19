"""
20.07.09
2754번 문제 코드에서 좀 더 복잡하게!
일사천리로 가다가 반올림이 막히네..
round 내장함수는 ROUND_HALF_EVEN 이라서 예제 입력1을 입력하면 3.27이 나오게 됨.
근데 문제에서는 ROUND_HALF_EVEN 이 아니라 ROUND_HALF_UP 을 원함.
round()를 쓸 수 없다는 뜻이고 ..

20.07.14
구글링해서
https://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221551624153
에서 my_round 라는 메소드를 가져와서 사용해보았음.
보통 알고 있는 반올림법을 적용해주는 메소드라고 하는데,,, 불필요한 코드는
삭제하고 적용해보았음.
일단 예제 입력1을 입력하면 3.28로 맞게 나오긴하는데 제출하니까 틀렸대.
소수점 아래 수가 하나만 있으면 어떻게 나오는지 테스트 해봐야겠음.
1.5, 2 를 인자로 넣으니까 역시나 1.5가 나왔음.
소수점 아래가 한 자리수일때만 처리해주는 코드를 만들면 될 것 같음.
0만 뒤에 붙여서 print 찍어주니까 바로 맞음요! 약간 야매끼가 있긴한데 ,,,
"""
from decimal import Decimal, ROUND_HALF_UP


def my_round(in_number, ndigits=0):
    expression = '0.' + '0' * ndigits
    number = in_number
    round_number = Decimal(number).quantize(Decimal(expression), rounding=ROUND_HALF_UP)

    # return number
    if ndigits > 0:
        return float(round_number)
    else:  # 0 or negative
        return int(round_number * (10 ** (-ndigits)))


def hakjum(sc: str):
    tscore = 0.0
    alpha = sc
    if alpha[0] == 'A':
        tscore += 4
    elif alpha[0] == 'B':
        tscore += 3
    elif alpha[0] == 'C':
        tscore += 2
    elif alpha[0] == 'D':
        tscore += 1
    else:
        return tscore
    if alpha[1] == '+':
        tscore += 0.3
    elif alpha[1] == '-':
        tscore -= 0.3
    return tscore


num_of_subjects = int(input())
subjectList = []
scoreSum = 0.0
weightSum = 0
for _ in range(num_of_subjects):
    name, weight, score = map(str, input().split(' '))
    subjectList.append([name, weight, score])
    scoreSum += float(weight) * hakjum(score)
    weightSum += float(weight)
res = scoreSum / weightSum
res = str(res)
if len(res) == 3 and res[1] == '.':
    res += '0'
    print(res)
else:
    print(my_round(res, 2))
