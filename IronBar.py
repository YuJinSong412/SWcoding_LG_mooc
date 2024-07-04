import sys
str_stick = sys.stdin.readline().rstrip()

count, store, temp = 0, 0, 0

for i in range(len(str_stick)):
    if i == len(str_stick)-1:
        continue
    if str_stick[i] == "(" and str_stick[i+1]=="(":
        count += 1
        if temp == 1:
            continue
        temp += 1
    elif str_stick[i] == "(" and str_stick[i+1] == ")":
        temp = 0
        store += count
    elif str_stick[i] == ")" and str_stick[i+1] == ")":
        store += 1
        count -= 1
        temp = 0
    else:
        continue

        
print(store)
