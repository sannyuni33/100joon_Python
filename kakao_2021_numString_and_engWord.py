def solution(s):
    ll = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for l in list(ll.keys()):
        while l in s:
            s = s.replace(l, ll[l])   
    return int(s)

# zero 부터 nine 까지 들어있는 리스트를 만들고.
# for i in 리스트: 해서 i가 문자열에 있으면 숫자로 교체?
# 전체 다 교체되는지 하나만 되는지 봐야함
# 한 번만 걸리는 듯 하다. while을 활용해보자

solution("one4seveneight")
solution("23four5six7")
solution("2three45sixseven")
solution("123")