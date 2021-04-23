def solution(citations):
    answer = 0
    cc = sorted(citations)
    num = len(cc)

    if cc[0] >= num:
        return num
    for i in range(num-1, 0, -1):
        if cc[num-i] >= i:
            answer = i
            break  # 최대값 찾았으니 종료
    return answer


solution([0, 0, 0])

# 논문의 수: len(citations)
# 논문별 인용 횟수: for x in citations
# 첨부터 끝까지 0 이면 0 도 나올 수 있음
# 예제 citations 의 [2]가 6이 아니라 10,000 이어도 답은 똑같이 3이다.
# H 인덱스의 최대값은 논문의 수.
# len(citations) 값부터 내려가면서 구해보기.

# 테스터 1부터 15까진 다 맞는데, 16에서 런타임에러가 난다?
# 반례를 찾아보자
# 0만 때려박았을때, answer 초기화가 되어있지 않아서 런타임에러가 났다.ㅜ