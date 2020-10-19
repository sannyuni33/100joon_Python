def solution(answers):
    answer = []
    corrects = [0, 0, 0]  # 세 명 각각의 정답 갯수 카운팅
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for x in range(len(answers)):
        if ans1[x % 5] == answers[x]:
            corrects[0] += 1
        if ans2[x % 8] == answers[x]:
            corrects[1] += 1
        if ans3[x % 10] == answers[x]:
            corrects[2] += 1

    # corrects 의 요소

    for i in range(3):
        if corrects[i] == max(corrects):
            answer.append(i+1)

    return answer


ans1 = [1, 2, 3, 4, 5]
ans2 = [1, 3, 2, 4, 2]
solution(ans2)

# answers 와 len(answers)를 매개변수로 받는 함수를 세 개 정의.(수포자1, 2, 3)
# 적절하게 반복문을 구성해서 비교하면 누가 많이 맞았는지는 구할 수 있을 것 같은디

# 첫 번째로는 answers 를 적절히 슬라이싱 하는 방법을 고민해야 함.
# 수포자1은 5길이, 2는 8길이, 3은 10길이로 반복을 하는데.
# 분명히 초과된 길이가 나올것이란 말임.
# answers 의 원소가 소진될때까지 del? 은 너무 무식하고.
# 5길이, 8길이, 10길이의 리스트를 계속해서 돌아가면 되니깐.
# 원형 큐에서 했던 것처럼 % 연산자를 활용하면 될듯.

# 그러면 함수 따로 정의 안해줘도 될 것 같은디.

