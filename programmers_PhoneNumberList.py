def solution(phone_book):
    answer = True
    return answer


solution(["119", "97674223", "1195524421"])
# solution(["123", "456", "789"])
# solution(["12", "123", "1235", "567", "88"])

# 다른 번호의 접두어인 경우가 하나라도 있으면 False 를 리턴하고 끝내기.
# 0번째 숫자로 분류를 하면? ([0]은 1로 시작하는 숫자, [1]은 2로 시작...)
# 그러면 다른 행에 있는 숫자의 접두사가 될 수가 없다.
# 이렇게 나눠도 최악의 경우를 생각하면,
# 1로 시작하는 100만개의 전화번호가 모두 20의 길이를 가진 경우.
# 같은 전화번호는 없다 했으니 나눠주는 의미가 없다고 봐도 무방하다.
#