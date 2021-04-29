from itertools import combinations as cb

def solution(clothes):
    answer = 0
    closet = {}
    for c in clothes:
        if c[1] not in list(closet.keys()):
            closet[c[1]] = [c[0]]
        else:
            closet[c[1]].append(c[0])
    print(closet)

    for i in range(1, len(closet)):
        choose_category = list(cb(list(closet.keys()), i))
        print(choose_category)

    return answer


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ['circle_glasses', 'eyewear'], ['black_sunglasses', 'eyewear'], ['blue_tshirt', 'top'], ['jeans', 'bottom'], ['long_coat', 'outer']])

# clothes 의 각 요소는 [의상, 종류] 이렇게 이루어져 있다.
# 그러면 딕셔너리를 {종류1 : [의상1, 의상2, ...], 종류2 : [의상1, 의상2, ...]...}
# 요렇게 만들 수 있다.

# 첫번째로, 몇 종류의 의상을 입을건지 결정 -> combination 활용
# 두번째로, 종류가 결정되면 그 종류에 있는 의상의 가짓수들을 곱해서 결과에 합산
