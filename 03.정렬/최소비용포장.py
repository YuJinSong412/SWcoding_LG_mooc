import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    package = list(map(int,readl().split()))
    return N, package
 
 
sol = -1
# 입력받는 부분
N, package = Input_Data()
 
# # 여기서부터 작성
def Solve():
    sum = 0                                                                                                                                                                                                  
    for i in range(N-1):
        package.sort()
   
        package[i+1] = package[i] + package[i+1]
        sum += package[i+1]
    return sum
     
sol = Solve()
 
 
# # 출력하는 부분
print(sol)
