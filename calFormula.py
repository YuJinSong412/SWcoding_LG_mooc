import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = list(map(int, str_exp[0::2]))
    op = str_exp[1::2]
    return N, nums, op

def Solve():
    stack = deque()
    stack.append(nums[0])
    for o, n in zip(op, nums[1:]):
        if o == "+" : stack.append(n)
        elif o == "-" : stack.append(-n) 
        elif o == "*" : stack[-1] = stack[-1] * n
        elif o == "/" : stack.append(int(stack.pop()/n))
   
    sum_result = 0 
    while stack:
        sum_result += stack.pop()

    return sum_result
sol = -1  
N, nums, op = Input_Data()

sol = Solve()

print(sol)
