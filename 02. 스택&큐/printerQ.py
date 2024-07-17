import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    num, index = map(int, readl().split())
    lists = list(map(int, readl().split()))

    return num, index, lists



T = int(sys.stdin.readline())

answer = []
for _ in range(T):
    num, index, lists= Input_Data() # 4, 2, [1,2,3,4]

    listss = []
    queue = deque()
    for i in range(len(lists)):
        queue.append((i,lists[i]))

    cnt = 0
    result = 0
    while len(queue) > 0:
        firstIndex = queue[0][0]
        firstNum = queue[0][1] # 1
        temp = firstNum

        for i in range(1,len(queue)): #1~3
            if temp <= queue[i][1]:
                temp = queue[i][1]
        
        if firstNum < temp:
            queue.popleft()
            queue.append((firstIndex, firstNum))
        elif firstNum >= temp:
            queue.popleft()
            listss.append((firstIndex, firstNum))
    
    
    for i in range(len(listss)):
        cnt += 1
        if listss[i][0] == index:
            result = cnt

    answer.append(result)
    

print(*answer,sep='\n')