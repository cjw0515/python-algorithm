"""
이분 검색

임의의 N개의 숫자가 입력으로 주어집니다. N개의 수를 오름차순으로 정렬한 다음 N개의 수
중 한 개의 수인 M이 주어지면 이분검색으로 M이 정렬된 상태에서 몇 번째에 있는지 구하는
프로그램을 작성하세요. 단 중복값은 존재하지 않습니다


"""

def exec(arr, m):
    n = len(arr)
    lt = 0
    rt = n - 1
    arr.sort()
    print(arr)

    while lt <= rt:
        mid = (lt + rt) // 2
        print(lt, mid, rt)
        if arr[mid] == m:
            print(mid + 1)
            break
        elif arr[mid] > m:
            rt = mid - 1
        else:
            lt = mid + 1







exec([23, 87, 65, 12, 57, 32, 99], 65)