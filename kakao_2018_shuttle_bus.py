def solution(n, t, m, timetable):
    answer = ''
    tmp = 540  # + t*(n-1)
    bus = str(tmp // 60).zfill(2)+':'+str(tmp % 60).zfill(2)
    timetable.sort()
    print(timetable)

    while n > 0:  # 버스 운행횟수만큼 반복
        print('버스도착:', bus)
        lastBus = []
        for _ in range(m):  # 일찍 온 순서대로 최대 m 명까지 태움
            if len(timetable) > 0 and timetable[0] <= bus:
                crew = timetable.pop(0)
                lastBus.append(crew)
                print(crew, '얘는 탔음')
        print('현재 정류장 모습:', timetable)
        print('아까 간 버스:', lastBus)
        tmp += t
        bus = str(tmp // 60).zfill(2) + ':' + str(tmp % 60).zfill(2)
        n -= 1
    print('버스 운행 완료')
    tmp -= t
    bus = str(tmp // 60).zfill(2) + ':' + str(tmp % 60).zfill(2)

    if len(lastBus) < m:  # 마지막 버스에 자리 남았음
        print('자리 남음!')
        answer = bus
    else:
        print('새치기 ㅎ')
        h, m = lastBus[-1].split(':')
        lt = int(h)*60 + int(m) - 1
        ss = str(lt // 60).zfill(2) + ':' + str(lt % 60).zfill(2)
        answer = ss
    print(answer)
    return answer


solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])

# 버스가 오고, 도착해있는 사람을 태우는것을 구현한다.
# 마지막 버스가 사람을 다태웠을때, 자리가 남으면 그 버스의 도착시간.
# 자리가 안남으면 마지막으로 탄사람보다 1분 일찍.