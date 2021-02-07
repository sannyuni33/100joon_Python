def solution(str1, str2):
    answer = 0
    if len(str2) < len(str1):
        str1, str2 = str2, str1
    str1, str2 = str1.lower(), str2.lower()
    set1, set2, gyo = [], [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set2.append(str2[i]+str2[i+1])
    print(set1)
    print(set2)
    # for i in range(len(set1)):
    #     for j in range(len(set2)):
    #         if set1[i] ==

    return answer


solution("FRANCE", "french")

# 중복을 허용하는 다중집합이기때문에 set() 으로 만들어버리면 곤란
# set1의 각 요소에 대해 set2의 각 요소와 비교, 일치하는애를 찾으면
# set1과 set2에서 둘 다 pop 하고 교집합에 집어넣는다,
# 교집합의 크기는 len(gyo), 합집합의 크기는 len(gyo)+len(set1)+len(set2)