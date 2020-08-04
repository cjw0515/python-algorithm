import math as m
import random
from functools import reduce
"""
    자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
    만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 
"""

def exec(m, n):
    cnt = 0
    for i in range(2, n+1):
        if m[i] == 0: cnt += 1
        for j in range(i , n+1, i):
            m[j] = 1

    return cnt


if __name__ == "__main__":
    # n = random.randint(1, 200000)
    n = 20
    n_arr = [0] * (n + 1)

    print(exec(n_arr, n))
    # print('result: ', exec(m))


