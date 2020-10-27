"""
20.07.09
답이야 맞았지만 뭐 1학년 1학기때 맨처음 하던 방식으로 하는게 맞는건지 싶네
코드 확 줄일 수 없나...
메소드 정의해서 첫번째 글자 두번째 글자로 나누니까 몇 줄 줄이긴 했음.
코드길이 467B -> 391B
"""
def hakjum():
    score = 0.0
    alpha = input()
    if alpha[0] == 'A':
        score += 4
    elif alpha[0] == 'B':
        score += 3
    elif alpha[0] == 'C':
        score += 2
    elif alpha[0] == 'D':
        score += 1
    else:
        print(score)
        return
    if alpha[1] == '+':
        score += 0.3
    elif alpha[1] == '-':
        score -= 0.3
    print(score)
hakjum()