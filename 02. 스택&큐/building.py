import sys
from collections import deque

def input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    height = [int(readl()) for _ in range(N)]
    return N, height

N, height = input_Data()

# # O(N^2) : Time Limit Exceed
# result = []
# for i in range(len(height)-1):
#     count = 0
#     for j in range(i+1, len(height)):
#         if height[i] < height[j]:
#             result.append(j+1)
#             count += 1
#     if count == 0:
#         result.append(0)
# result.append(0)        

# print(*result, sep="\n")

sol_list = [0] * (N+1)

stack = deque()

for i, h in enumerate(height,1):
    while stack and stack[-1][1] < h:
        sol_list[stack[-1][0]] = i
        stack.pop()
    stack.append((i,h))

print(*sol_list[1:], sep="\n")
