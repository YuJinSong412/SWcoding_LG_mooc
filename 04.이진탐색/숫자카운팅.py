import sys
import bisect

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = list(map(int, readl().split()))
    M = int(readl())
    query = list(map(int, readl().split()))

    return N, num, M, query


def binary_search_lower(start, end, target):
    sol = -1
    while start <= end:
        mid = (start+end)//2
        if num[mid] == target:
            sol = mid
            end = mid - 1
        elif num[mid] > target:
            end = mid -1
        else:
            start = mid+1
    return sol


def binary_search_upper(start, end, target):
    sol = -1 
    while start <= end:
        mid = (start + end)//2
        if num[mid] == target:
            sol = mid
            start = mid + 1
        elif num[mid] > target:
            end = mid -1
        else:
            start = mid+1
    return sol

def Solve():
    sol = []

    for q in query:
        lower = binary_search_lower(0, len(num)-1, q)
        if lower == -1:
            sol.append(0)
        else:
            upper = binary_search_upper(0,len(num)-1, q)
            sol.append(upper-lower+1)
    return sol

def Solve_bisect():
    sol = []
    for q in query:
        lower = bisect.bisect_left(num,q)
        if lower != len(num) and num[lower] == q:
            upper = bisect.bisect_right(num,q)
            sol.append(upper-lower)
        else: sol.append(0)
    return sol

sol = []
N, num, M, query = Input_Data()

# sol = Solve()
sol = Solve_bisect()

print(*sol)