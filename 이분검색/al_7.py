"""
창고 정리

창고에 상자가 가로방향으로 일렬로 쌓여있습니다.
창고의 가로 길이와 각 열의 상자 높이가 주어집니다. m 회의 높이 조정을 한 후 가장 높은 곳과 가장 낮은 곳의 차이를 출력하는 프로그램을 작성하세요.

"""

def exec(s, m):
    s = list(map(int, s.split()))
    for _ in range(m):
        s.sort()
        s[0] += 1
        s[len(s) - 1] -= 1

    return max(s) - min(s)


res = exec("69 42 68 76 40 87 14 65 76 81", 50)
print(res)