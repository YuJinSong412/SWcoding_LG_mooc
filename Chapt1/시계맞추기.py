INF = float('inf')

# 각 스위치가 조작하는 시계의 목록
switches = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]

# 모든 시계를 12시로 맞추는 최소 스위치 조작 횟수를 찾는 함수
def solve(clocks, switch_index):
    # 만약 모든 스위치를 검사했다면, 모든 시계가 12시인지 확인
    if switch_index == len(switches):
        return 0 if all(clock == 12 for clock in clocks) else INF
   
    # 현재 스위치를 0번, 1번, 2번, 3번 누르는 경우에 대해 재귀적으로 탐색
    min_moves = INF
    for count in range(4):
        min_moves = min(min_moves, count + solve(clocks, switch_index + 1))
        # 스위치를 누른 횟수만큼 해당 시계를 3시간씩 이동
        for clock in switches[switch_index]:
            clocks[clock] = (clocks[clock] % 12) + 3

    # 되돌리기 위해 다시 스위치를 누른 횟수만큼 시계를 되돌림
    for _ in range(4):
        for clock in switches[switch_index]:
            clocks[clock] = (clocks[clock] - 3) % 12 if (clocks[clock] - 3) != 0 else 12

    return min_moves

# 예제 시계 상태 (모두 12시가 되어야 함)
clocks = [12, 6, 6, 6, 9, 12, 6, 12, 9, 12, 12, 12, 12, 12, 12, 12]

# 최소 스위치 조작 횟수 출력
result = solve(clocks, 0)
print(result if result != INF else -1)