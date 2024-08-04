import sys
  
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M

def Solve():
    needs.sort()
    sol = -1
    
    start = needs[0]
    end = needs[N-1]
    
    while start <= end:
        mid = (start + end) // 2
        
        sum = 0
        for n in needs:
            if mid > n:
                sum += n
            else:
                sum += mid
        
        if sum == M:
            sol = mid
            break
        elif sum > M:
            end = mid -1
        else:
            sol = mid
            start = mid + 1
    return sol

sol = -1
N, needs, M = Input_Data()
sol = Solve()
print(sol)