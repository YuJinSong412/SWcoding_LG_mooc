#https://www.acmicpc.net/problem/5585
# 500 100 50 10 5 1 

import sys

readl = sys.stdin.readline
coin = int(readl())

n = 1000
cnt = 0

coins = [500,100,50,10,5,1]

target = n - coin
for coin in coins:
    cnt += target // coin
    target %= coin

print(cnt)

