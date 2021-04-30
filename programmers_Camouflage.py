def solution(clothes):
    answer = 1
    closet = {}
    for c in clothes:
        if c[1] not in list(closet.keys()):
            closet[c[1]] = 2
        else:
            closet[c[1]] += 1

    for x in closet.values():
        answer *= x

    print(answer-1)
    return answer-1


# solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ['circle_glasses', 'eyewear'], ['black_sunglasses', 'eyewear'], ['blue_tshirt', 'top'], ['jeans', 'bottom'], ['long_coat', 'outer']])
# solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])

# clothes 의 각 요소는 [의상, 종류] 이렇게 이루어져 있다.
# 그러면 딕셔너리를 {종류1 : [의상1, 의상2, ...], 종류2 : [의상1, 의상2, ...]...}
# 요렇게 만들 수 있다.

# 첫번째로, 몇 종류의 의상을 입을건지 결정 -> combination 활용, choose_category 에 저장
# 두번째로, 종류가 결정되면 그 종류에 있는 의상의 가짓수들을 곱해서 결과에 합산

# ... 이렇게 했더니 28개 테스트케이스 중 1번만 시간초과... 이건 걍 틀린거다.
# 어느 부분이 부담이 됐을래나. 아무래도 3중 for 문이 그렇지 않았을래나.

# closet 에다가 옷 종류를 일일히 써주지 말고 그냥 가짓수만 저장하면 안돼냐!!!!
# 같은 이름 의상 없다매 !!!
# 그래도 삼중 for 문 구조는 그대로지만, 일단 시도............역시나 실패요

# key 를 가지고 조합을 구하지말고 애초에 value 를 가지고 조합을 구한다면,
# 같은 가짓수를 가진 종류가 중복때문에 삭제되지 않나.? 아니잔항!!!!!!!!!!!!!!!

# 그렇게 해서 나온 각 조합에 요소 곱을 해주려고 np.prod 를 적용했더니,
# 직접 for 문 돌린거보다 시간이 더 오래걸린다............. 뻐큐

# 결국 오픈소스를 참고했고, 어떤 종류는 입고 안입고를 combination 으로 구한게아니라
# 각 종류별로 +1을 더해줘서 안입은 경우를 추가해주고, 각 value 를 곱한다.
# 그 다음에 아무것도 안입은 경우를 고려해 최종 결과에서 -1을 빼니까 정답.
# ..............후