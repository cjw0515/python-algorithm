"""
회의실 배정(그리디)



"""

def exec(s: list, m):

    s = list(map(lambda x: tuple(x), s))
    s.sort(key=lambda x: x[1])

    selected_meetings = [s[0]]
    pre_time = s[0]

    for time in s:
        if pre_time[1] <= time[0]:
            pre_time = time
            selected_meetings.append(time)

    return selected_meetings


res = exec([[1, 4], [2, 3], [3, 5], [4, 6], [5, 7]], 5)
print(res)