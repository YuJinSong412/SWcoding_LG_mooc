import sys
num = int(sys.stdin.readline().rstrip())

results = {0:'0/1', 1:'1/1'}

for i in range(2,num+1):
    for j in range(1, i): 
        temp = j / i
        if temp in results.keys():
            continue
        results[temp] = str(j)+"/"+str(i)

sort_results = dict(sorted(results.items()))
ans = sort_results.values()

print(*ans, sep="\n")
