import heapq as hq


def solution(jobs):
    ans1 = ans2 = currTime = 0
    scheduler = []
    # hq.heapify(scheduler)  # 작업 대기중인 애들
    # jobs.sort()  # 작업 요청시점으로 정렬 안된 테스트 케이스가 있다면 이 주석을 푸삼!
    while jobs or scheduler:

        if jobs[0][0] <= currTime:  # 현재 시간보다 요청시간이 빠른작업은 모두 대기
            print('before scheduling:', jobs)
            tmp = jobs.pop(0)
            scheduler.append(tmp[::-1])
            # hq.heappush(scheduler, tmp[::-1])  # 소요시간을 기준으로 힙 구성
            print('after scheduling:', jobs)
        else:
            if scheduler:  # 이미 요청시간 저기한 애들만 들어와있음.
                # completed = hq.heappop(scheduler)
                scheduler.sort()
                print('scheduler:', scheduler)
                completed = scheduler.pop(0)
                print(completed, 'has complete')
                ans1 += currTime + completed[0] - completed[1]
                ans2 += 1  # 완료된 작업 수
                currTime += completed[0]
                print('time:', currTime)
            else:  # 대기중인 작업 없음
                currTime += 1
                print('time:', currTime)
            continue
        if not len(jobs):
            # break 가 아니라 스케줄러에 남아있는 애들 처리해야 함
            break
    print(ans1 // ans2)
    return ans1 // ans2


solution([[0, 3], [1, 9], [2, 6]])
# solution([[0, 3], [20, 9], [10, 6], [2, 5], [5, 8]])


# 1. 작업을 언제 넣고 언제 뺄지를 명확하게 정의해야한다.
# 2. 작업의 어느정보를 넣고 뺄지도 정의를 잘 해줘야한다.

# 최소힙을 사용하고, 노드의 대소 비교는 job[i][1]이 기준이어야 함.
# jobs 에 작업들이 존재하는 동안 반복문을 돌리면서 시간을 1씩 늘린다.
# 시간과 job[0]이 일치할때 힙에 넣어야한다.
