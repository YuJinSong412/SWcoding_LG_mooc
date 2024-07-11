import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	return N


N = Input_Data()
lists = deque()


for i in range(1,N+1):
	lists.append(i)

sendLists = []

while len(lists) > 0:
	temp = lists[-1] // 2 
	
	for i in range(temp):
		firstNum = lists[0]
		lists.popleft()
		lists.append(firstNum)
	sendLists.append(lists[0])
	lists.popleft()

print(*sendLists)