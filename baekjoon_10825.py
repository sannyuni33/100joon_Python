from sys import stdin
n = int(stdin.readline())
stdList = []
for _ in range(n):
    name, kor, eng, math = map(str, stdin.readline().split(' '))
    stdList.append({'name': name, 'kor': int(kor), 'eng': int(eng), 'math': int(math)})
result = sorted(stdList, key=lambda e: (-e['kor'], e['eng'], -e['math'], e['name']))
for x in result:
    print(x['name'])

# 두 가지 접근방식이 떠오름.
# 1. 입력받을 때 아예 맞는 자리에 넣어버리기
# 2. 일단 입력 받고 나서 정렬하기
# 최대 입력 회수는 10만이니까 이중 for 문 쓰거나하면 1초는 무조건 넘겠고...
# 이름, 국어, 영어, 수학 이 리스트나 튜플 등으로 묶여져있어야 좋지 않을까?
# 데이터프레임 써봐야 할래나
# 아니면, 2차원 배열을 사용? 2중 for 문의 가능성이 예상되지만 일단 고민해보는 중
# 딕셔너리 리스트 자료구조에 sorted 와 lambda 를 활용하면 끝난다?
# 허걱... 592ms로 해결되었습니다