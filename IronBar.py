import sys
str_stick = sys.stdin.readline().rstrip()

def Solve(str_stick):
    stick = 0
    count = 0

    for i in range(len(str_stick)):
        if str_stick[i] == "(":
            stick +=1
        else:
            stick -= 1
            count += stick if str_stick[i-1]=="(" else 1
    
    return count

ans = -1

ans = Solve(str_stick)

print(ans)
