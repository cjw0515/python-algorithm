import math as m
"""
 두 개의 정 N면체와 정 M면체의 두개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
 정답이 여러 개일 경우 오름차순으로 출력합니다.
"""

def exec(m, n):
    cnt_arr = [0] * (m + n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cnt_arr[i + j] += 1

    max = 0
    for idx, i in enumerate(cnt_arr, 0):
        if max <= i:
            max = i
    for idx, i in enumerate(cnt_arr, 0):
        if i == max:
            print(idx)

    return


if __name__ == "__main__":
    m = 6
    n = 4
    exec(m, n)


