import math as m
import random
from functools import reduce
"""
    뒤집은 소수
    N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수 가 소수이면 그 수를 출력하는 프로그램을 작성하세요.
    예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다 , 단 910을 뒤집으면 19로 숫자화 해야한다. 
    첫 자리부터의 연속된 0은 무시한다. 뒤집는 함수, 소수 여부 확인함수를 반드시 작성한다. 
"""

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

def revers(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res

def exec(m):
    for n in m:
        tmp = revers(n)
        if is_prime(tmp):
            print(tmp)

if __name__ == "__main__":
    n = 3
    m = []
    for i in range(n):
        m.append(random.randint(1, 100000))

    exec([1842])
    # print('result: ', exec(m))



