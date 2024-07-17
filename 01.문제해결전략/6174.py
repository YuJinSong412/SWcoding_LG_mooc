import sys

def Input_Data():
    read1 = sys.stdin.readline
    num = int(read1())
    return num

ans = -1

# #입력 받는 부분
num = Input_Data()

# 2008
# sort해서 값을 내고 
# num에 그 값을 다시 저장해서
# 계속 반복하도록 만든다. 
# 6174이면 멈추기
count = 0
while True:
    if num == 6174:
        ans = count
        break

    count += 1
    listNum = list(map(int, str(num)))
    sortedReverseNum = sorted(listNum, reverse=True)
    sortedNum = sorted(listNum)

    #숫자형 리스트를 단일 값으로 병합하기
    result2 = ''.join(map(str,sortedReverseNum))
    resultInt2 = int(result2)

    result = ''.join(map(str,sortedNum))
    resultInt = int(result)

    finals = resultInt2 - resultInt
    num = finals


print(ans)
