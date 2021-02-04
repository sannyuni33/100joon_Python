def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    set1, set2 = [], []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            set1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            set2.append(str2[i]+str2[i+1])
    print(set1)
    print(set2)

    return answer


solution("FRANCE", "french")

# 중복을 허용하는 다중집합이기때문에 set() 으로 만들어버리면 곤란
#