import math as m
"""
 N명의 학생의 수학성적이 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
 N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
 답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다.
"""

def exec(arr):
    avg = round(sum(arr) / len(arr))

    cl_diff = 100

    for idx, score in enumerate(arr):
        diff = abs(avg - score)

        if diff < cl_diff:
            res = idx + 1
            cl_diff = diff
            tmp_score = score
        elif diff == cl_diff:
            if tmp_score < score:
                res = idx + 1
                tmp_score = score

    return avg, res


if __name__ == "__main__":
    """
    10
    65 73 66 87 92 67 55 79 75 80
    """
    arr = [65, 73, 66, 87, 92, 67, 55, 99, 78, 99]
    print(exec(arr))