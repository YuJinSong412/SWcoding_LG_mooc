import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = list(map(int, readl().split()))
    T = int(readl())
    query = list(map(int, readl().split()))
    return N, num, T, query

def binary_search(array, target, start,end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return 0



N, num, T, query = Input_Data()

for i in range(T):
    index = binary_search(num, query[i], 0, N-1)
    if index == 0:
        print(index)
    else:
        print(index+1)