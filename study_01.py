def solution(numbers):
    answer = []
    pair_dict = {}
    num_of_thousand = 0

    for x in numbers:
        if x < 10:
            pair_dict[str(x)] = x*1000
        elif x < 100:
            pair_dict[str(x)] = x*100
        elif x < 1000:
            pair_dict[str(x)] = x*10
        else:
            num_of_thousand += 1

    pair_list = sorted(pair_dict.items(), key=lambda t: t[1], reverse=True)
    pair_dict = dict(pair_list)

    for x in pair_dict.keys():
        answer.append(x)

    for _ in range(num_of_thousand):
        answer.append('1000')

    answer = ''.join(answer)
    print(answer)
    return answer


nums1 = [6, 10, 2]
nums2 = [3, 30, 34, 5, 9]
nums3 = [3, 30, 34, 5, 9, 1000]
solution(nums3)

# 가능한 모든 경우의 수를 만들고 정렬하는 건 말도 안되고
# 세 자릿수, 두 자릿수, 한 자릿수로 나눠서 정렬.
# 999, 99, 9 가 먼저 나와야 하고.
# 998, 997 ~ 990 까지 나오고 98
# 근데 989~980보다 98이 먼저 나오는게 나음.
# 이게 뭘 의미하냐면 999, 99, 9 순이 아니라 9, 99, 999(~ 990) 순이 맞다는 것을 의미하는 듯.
# 근데 한 숫자가 두 번 이상 나오는 것도 가능함.
# 9가 루트고 두 자릿수가 레벨2, 세 자릿수가 레벨3인 트리 형태 ...로 만들어서 카운팅 해야하나.
# 파이썬에서 만들려면 리스트 컴프리헨션 써서 0으로 초기화 된 삼중첩 리스트
# 로 만들면 세 자릿수만 셀 수 있는거 아닌가

# '8'이 최초로 나오는 시점은 트리 그려본대로 하면 900 다음

# 한 자릿수에서 '9'가 나왔을 때, 두 자릿수에서 '9'로 시작하는 애만 나오게.
# 두 자릿수에서 '99'가 나왔을 때, 세 자릿수에서 '99'로 시작하는 애만 나오게.
# 같은 수 여러 번 나올 수 있으니까 '9'나 '99'로 시작하는 애들은 다 나오게 해야함.
# 한 자릿수에는 8이 없는데 두 자릿수는 '8n'이 있는 이런 경우도 생각을 해야함
# 아 잠시만 무조건 한 자릿수 두 자릿수 세 자릿수 순서가 아니네

# 1000 제외한 모든 수를 네 자릿수로 만들어버리고, 큰 순서대로 정렬하면 어떨지.
# {원래수:네 자릿수}로 짝을 지어준 뒤, 네 자릿수 기준으로 정렬. 후 원래수를  answer 에 append 하면?

