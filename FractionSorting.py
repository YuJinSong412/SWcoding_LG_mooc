import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N

N = Input_Data() 

my_dict = {0:'0/1', 1:'1/1'}
for i in range(2, N+1):
    for j in range(1,i):
        temp = j / i
        if temp in my_dict.keys():
            continue
        my_dict[temp] =str(j)+'/'+str(i) 


sort_list = dict(sorted(my_dict.items()))
result = sort_list.values()

print(*result, sep="\n")
