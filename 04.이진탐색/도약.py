import sys
import bisect

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    return N, pos

def binary_search_lower(start, end, target):
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if pos[mid] >= target:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    return ans

def binary_search_upper(start, end, target):
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if pos[mid] <= target:
            ans = mid
            start = mid + 1
        else:
            end = mid -1 
    return ans


    
def Solve():
    pos.sort()
    cnt = 0
    
    for s1 in range(N-2):
        for s2 in range(s1+1, N-1):
            jump = pos[s2] - pos[s1]
            min = pos[s2] + jump
            max =  pos[s2] + 2 * jump
            lower = binary_search_lower(s2+1, N-1, min)
            if lower == -1 or pos[lower] > max: continue
            upper = binary_search_upper(s2+1,N-1,max)
            cnt += upper - lower + 1

    return cnt
            
def Solve_2():
    pos.sort()
    cnt = 0
    
    for s1 in range(N-2):
        for s2 in range(s1+1, N-1):
            jump = pos[s2] - pos[s1]
            min = pos[s2] + jump
            max = pos[s2] + 2 * jump
            lower = bisect.bisect_left(pos, min)
            if lower == len(pos) or pos[lower] > max: continue
            upper = bisect.bisect_right(pos, max)
            cnt += upper - lower 

    return cnt

sol = -1
N, pos = Input_Data()

sol = Solve()
# sol = Solve_2()
print(sol)

