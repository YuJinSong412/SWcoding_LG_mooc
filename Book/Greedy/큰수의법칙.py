import sys

readl = sys.stdin.readline

def Input_Data():
    readl = sys.stdin.readline
    info = list(map(int, readl().split()))
    N = info[0]
    M = info[1]
    K = info[2]
    datas = list(map(int, readl().split()))
    return N, M, K, datas

def Solve():
    datas.sort(reverse=True)

    mulNum = M // (K + 1)
    addNum = M % (K+1)

    result = (datas[0] * K + datas[1]) * mulNum + datas[0] * addNum

    return result


N, M, K, datas = Input_Data()

sol = -1

sol = Solve()

print(sol)

