"""
마구간 정하기(결정 알고리즘)

N개의 마구간이 수직선상에 있습니다. 각 마구간은 x1, x2, x3, ......, xN의 좌표를 가지며, 마
구간간에 좌표가 중복되는 일은 없습니다.
현수는 C마리의 말을 가지고 있는데, 이 말들은 서로 가까이 있는 것을 좋아하지 않습니다.
각 마구간에는 한 마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되게 말을
마구간에 배치하고 싶습니다.
C마리의 말을 N개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대
값을 출력하는 프로그램을 작성하세요.

첫 줄에 자연수 N(3<=N<=200,000)과 C(2<=C<=N)이 공백을 사이에 두고 주어집니다.
둘째 줄부터 N개의 줄에 걸쳐 마구간의 좌표 xi(0<=xi<=1,000,000,000)가 한 줄에 하나씩
주어집니다.

"""

def exec(s, m):
    s.sort()
    res = None

    def get_horses(range):
        cnt = 1
        sp = s[0]
        for mgg in s:
            if mgg - sp >= range:
                cnt += 1
                sp = mgg
        return cnt

    lt = s[0]
    rt = s[len(s) - 1]

    while lt <= rt:
        mid = (lt + rt) // 2
        if get_horses(range=mid) >= m:
            res = mid
            print(res)
            lt = mid + 1
        else:
            rt = mid - 1

    return res





res = exec([1, 2, 8, 4, 9], 3)
print(res)