n = int(input())
wordList = []

for _ in range(n):
    tmp = input()
    wordList.append(tmp)
    if tmp[::-1] in wordList:
        ans1 = len(tmp)
        ans2 = tmp[ans1//2]
print(ans1, ans2)

# n개의 입력을 받는데, 비밀번호만 거꾸로 된 애가 존재함.
# 리스트 in 쓰면 끝나는거 아니고?
# 아스키코드 값을 비교하기에는, 같은 값을 가질 수 있는 애들이 넘 많고.
#