# 지뢰찾기는 n × n 격자 위에서 이루어진다. m개의 지뢰가 각각 서로 다른 격자 위에 숨겨져 있다. 플레이어는 격자판의 어느 지점을 건드리기를 계속한다. 지뢰가 있는 지점을 건드리면 플레이어가 진다. 지뢰가 없는 지점을 건드리면, 그곳의 상하좌우 혹은 대각선으로 인접한 8개의 칸에 지뢰가 몇 개 있는지 알려주는 0과 8 사이의 숫자가 나타난다. 완전히 플레이되지 않은 게임에서 일련의 동작이 아래에 나타나 있다.
# 여기서, n은 8이고, m은 10이며, 빈 칸은 숫자 0을 의미하고, 올라가 있는 칸은 아직 플레이되지 않은 위치이며, 별표 모양(*)과 닮은 그림은 지뢰를 의미한다. 맨 왼쪽의 그림은 일부만이 플레이된 게임을 나타낸다. 첫 번째 그림에서 두 번째 그림으로 오면서, 플레이어는 두 번의 이동을 시행해서, 두 번 다 안전한 곳을 골랐다. 세 번째 그림을 볼 때 플레이어는 운이 썩 좋지는 않았다. 지뢰가 있는 곳을 골라서 게임에서 졌다. 플레이어는 m개의 열리지 않은 칸을 남길 때까지 계속해서 안전한 곳을 고르면 이긴다. 그 m개의 칸은 반드시 지뢰이다.

# 당신이 할 일은 일부가 플레이된 게임의 정보를 읽어 해당하는 격자를 출력하는 것이다.

# 방향벡터 : 좌상/좌/좌하//하/상//우상/우/우하 순서
dx = [-1, -1, -1, 0, 0 ,1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


N = int(input())
board = [input() for _ in range(N)] # 지뢰판
press = [input() for _ in range(N)] # 누른부분
answer = [['.' for _ in range(N)] for _ in range(N)] # 출력
gamerun = False # 진행 가능?
for i in range(N): 
    for j in range(N):
        if press[i][j] == "x": # 누른부분이 X인데
            if board[i][j] == "*": #지뢰가 있으면 
                gamerun = True # 더이상 진행불가
            cnt = 0
            for k in range(8):
                x = i + dx[k] # i주변 벡터 반환
                y = j + dy[k] # j주변 벡터 반환
                if 0<= x < N and 0 <= y < N: # 판때기 내에 있으면서
                    if board[x][y] == "*": # 지뢰가 범위내?
                        cnt += 1 # 지뢰수만큼 추가
            answer[i][j] = str(cnt) # join쓰게 문자열로 추가
for i in range(N):
    print(''.join(answer[i]))
if gamerun: #진행 가능하면서
    for row in range(N):
        for col in range(N):
            if board[row][col] == "*": # 지뢰들도
                answer[row][col] = "*" # 표시
for i in range(N):
    print(''.join(answer[i]))