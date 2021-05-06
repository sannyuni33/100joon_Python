#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    #여기에 코드를 작성해주세요.
    answer = 0
    chessBoard = [[0 for _ in range(8)] for _ in range(8)]
    toFindRow = [-1, -1, 1, 1]  # 좌상, 우상, 우하, 좌하 순서로 탐색
    toFindCol = [-1, 1, 1, -1]
    for bishop in bishops:
        row, col = -(int(bishop[1])-8), ord(bishop[0])-65
        chessBoard[row][col] = 1
        for i in range(4):
            kr, kc = toFindRow[i], toFindCol[i]
            while -1 < row+kr < 8 and -1 < col+kc < 8:
                if not chessBoard[row+kr][col+kc]:
                    chessBoard[row + kr][col + kc] = 1
                    print(row + kr, col + kc, '에는 놓을 수 없삼!')
                kr += toFindRow[i]
                kc += toFindCol[i]
    for i in range(8):
        for j in range(8):
            if not chessBoard[i][j]:
                answer += 1
    return answer

# #아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")