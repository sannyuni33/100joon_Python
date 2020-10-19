"""
20.07.07
요놈을 어떻게 풀어볼까
처음에는 공백 리스트 만들고 n*m번 append 해준 다음
이중 for 문으로 출력하자는 방식으로 접근 시도.
모든 줄의 끝에 공백이 있으면 안되는 부분이 신경이 쓰임
좀 생각해보니까 이게 너무 파이썬스럽지가 않은것같음. 개 구데기임.
N*M 크기 행렬을 만드는 모듈이 있을텐데 -> numpy
아니다 넘파이도 필요없음 그냥 list comprehension 하면 됨요
20분정도 지나서 list comprehension 이랑 출력도 이쁘게 찍히는데
print('\b')로 줄바꿈 처리를 해주면 맨 마지막에 공백지우고 줄바꿈이 또 되는게
출력오류 요인. 이 넘을 어떻게 하면 좋을지 고민중임.
format 이라는 메소드가 있다는디, 이 넘에 대해서 공부좀 해보고 다시 해야겠다

20.07.08
공백과 줄바꿈을 아무리 고쳐도 계속 틀렸다고 나와서 멘붕이 왔음
뭐지 하면서 3 10을 입력으로 넣으니까
1 2 3 4 5 6 7 8 9 10
5 6 7 8 9 10
11 12 13 14 9 10
11 12 13 14 15 16 17 18
가 나왔음. 리스트를 잘못 만들었던거임........................................
list comprehension 에서 오류가 있었지.............
공백과 줄바꿈 알고리즘은 틀린게 아니었다....................

아놔 마지막 줄도 줄바꿈으로 끝내야 맞는거네
"""
n, m = map(int, input().split(' '))
mat = [[i+(j*m) for i in range(1, m+1)] for j in range(n)]

for row in mat:
    for num in row:
        if num % m != 0:
            print(num, end=' ')
        else:
            print(num)