def solution(genres, plays):
    answer = []
    songs = {}

    for i in range(len(genres)):
        if genres[i] in songs.keys():
            songs[genres[i]][1].append([plays[i], i])
            songs[genres[i]][0] += plays[i]
        else:
            songs[genres[i]] = [plays[i], [[plays[i], i]]]

    for li in list(songs.values()):
        li[1].sort(key=lambda x: (-x[0], x[1]))

    songs = sorted(songs.items(), key=lambda item: -item[1][0])

    for s in songs:
        for i in s[1][1][:2]:
            answer.append(i[1])

    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
# 첫 번째로 장르 순서를 정해야하고 그 다음엔 장르 내에서 노래 순서를 정해야한다
# 노래 순서는 재생횟수가 첫 번째 기준이고, 고유번호가 두 번째 기준이다. -> lambda 활용
