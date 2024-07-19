import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    score = map(int, readl().split())
    list_score = [[i,s] for i, s in enumerate(score,1)]
    return N, list_score


N,list_score = Input_Data()

list_score.sort(key = lambda x:-x[1])
sol = [list_score[0][0], list_score[1][0], list_score[2][0]]

print(*sol)