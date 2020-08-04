import math as m
import random
from functools import reduce
"""
 n개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하는 프로그램을 작성하세요.
 각 자연수의 합을 구하는 함수를 구하는 함수를 작성하시오.
"""

def exec(m):
    def idx_sum(num_arr):
        return reduce(lambda acc, crr: acc + crr, num_arr, 0)
    print(m)
    max = 0
    for n in m:
        res = idx_sum([int(x) for x in str(n)])
        print(res)
        if max < res: max = res

    return max


if __name__ == "__main__":
    n = 3
    m = []
    for i in range(n):
        m.append(random.randint(1, 10000000))

    print('result: ', exec(m))


