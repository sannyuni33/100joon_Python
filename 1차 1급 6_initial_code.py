#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0
    toFind_row = [-1, -2, -2, -1, 1, 2, 2, 1]
    toFind_col = [-2, -1, 1, 2, 2, 1, -1, -2]
    row, col = pos[1], pos[0]

    chessBoard = []
    for i in range(65, 73):
        for j in range(1, 9):
            chessBoard.append(str(i)+str(j))

    for i in range(8):
        tmpRow = int(row) + toFind_row[i]
        tmpCol = ord(col) + toFind_col[i]
        if str(tmpCol)+str(tmpRow) in chessBoard:
            answer += 1

    return answer

#The following is code to output testcase.
pos = "E4"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")