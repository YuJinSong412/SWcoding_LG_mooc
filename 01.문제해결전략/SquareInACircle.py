import sys
num = int(sys.stdin.readline().rstrip())

cnt = 0

for h in range(1,num+1):
    for w in range(1, num+1):
        temp = w*w + h*h
        if temp > num * num:
            continue
        cnt += 1

result = cnt *4
print(result)

