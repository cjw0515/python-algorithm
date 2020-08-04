import math as m
import random
from functools import reduce
"""
    1에서 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
    규칙 (1) 같은 눈이 3개가 나오면 10,000 + (같은 눈) * 1,000
    규칙 (2) 같은 눈이 2개만 나오는 경우에는 1,000원 +(같은 눈) * 100원의 상금을 받게된다.    
    규칙 (3) 모두 다른 눈이 나오는 경우에는(그 중 가장 큰 눈) * 100원의 상금을 받게 된다.
    
    예를 들어, 3개의 눈 3,3,6이 주어지면 1000+3*100으로 계산되어 1300원을 받게된다. 또 3개의 눈이 2,2,2로 주어지면 10000+2*1000으로
    계산되어 12000을 받게된다, 3개의 눈이 6,2,5로 주어지면 그 중 가장 큰 값이 6이므로 6*100으로 계산되어 600원을 상금으로 받게된다.
    
    가장 많은 상금을 받은 사람의 상금 출력
"""
def exec(dice_res):
    res = 0
    money = 0
    for r in dice_res:
        r.sort()
        a, b, c = r
        if a == b and b == c:
            money = 10000 + 1000 * a
        elif a == b or b == c:
            money = 1000 + b * 100
        elif a == c:
            money = 1000 + a * 100
        else:
            money = c * 100
            # max = 0
            # for n in r:
            #     if max < n: max = n
            # money = max * 100
        if res < money: res = money

    return res

if __name__ == "__main__":
    dice_res = [
        [3, 3, 6],
        [2, 2, 2],
        [6, 2, 5],
    ]

    print(exec(dice_res))