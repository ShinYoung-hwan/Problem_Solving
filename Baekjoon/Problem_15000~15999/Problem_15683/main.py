import sys

input = lambda: sys.stdin.readline().rstrip()

def count_blanks():
    cnt = 0
    for r in range(R):
        for c in range(C):
            cnt += (board[r][c] == 0)
    return cnt

def set_right(r0, c0, converted):
    global board
    for c in range(c0+1, C):
        if board[r0][c] == 6: break # 벽을 만난 경우 더이상 진행 불가
        if board[r0][c] != 0: continue # 이미 커버 가능한 위치인 경우
        
        converted.append((r0, c))
        board[r0][c] = -1
def set_up(r0, c0, converted):
    global board
    for r in range(r0-1, -1, -1):
        if board[r][c0] == 6: break # 벽을 만난 경우 더이상 진행 불가
        if board[r][c0] != 0: continue # 이미 커버 가능한 위치인 경우
        
        converted.append((r, c0))
        board[r][c0] = -1
def set_left(r0, c0, converted):
    global board
    for c in range(c0-1, -1, -1):
        if board[r0][c] == 6: break # 벽을 만난 경우 더이상 진행 불가
        if board[r0][c] != 0: continue # 이미 커버 가능한 위치인 경우
        
        converted.append((r0, c))
        board[r0][c] = -1
def set_down(r0, c0, converted):
    global board
    for r in range(r0+1, R):
        if board[r][c0] == 6: break # 벽을 만난 경우 더이상 진행 불가
        if board[r][c0] != 0: continue # 이미 커버 가능한 위치인 경우
        
        converted.append((r, c0))
        board[r][c0] = -1
set_direction = [ 
    set_right,
    set_up,
    set_left,
    set_down
]

def cctv1(dir, r0, c0, converted):
    set_direction[dir](r0, c0, converted)
    
def cctv2(dir, r0, c0, converted):
    set_direction[dir](r0, c0, converted)
    set_direction[dir+2](r0, c0, converted)
        
def cctv3(dir, r0, c0, converted):
    set_direction[dir](r0, c0, converted)
    set_direction[(dir+1)%4](r0, c0, converted)
    
def cctv4(dir, r0, c0, converted):
    set_direction[dir](r0, c0, converted)
    set_direction[(dir+1)%4](r0, c0, converted)
    set_direction[(dir+2)%4](r0, c0, converted)
    
def cctv5(dir, r0, c0, converted):
    set_direction[dir](r0, c0, converted)
    set_direction[(dir+1)%4](r0, c0, converted)
    set_direction[(dir+2)%4](r0, c0, converted)
    set_direction[(dir+3)%4](r0, c0, converted)
    
cctv_direction = [
    print, cctv1, cctv2, cctv3, cctv4, cctv5
]

def DFS(depth=0):
    global answer, board
    # base
    if depth == len(cctvs):
        cnt = count_blanks()
        answer = min(answer, cnt)
        return
    
    # default
    cctv, r0, c0 = cctvs[depth]
    if cctv == 2:
        for dir in range(2):
            converted = [] 
            cctv2(dir, r0, c0, converted)
            DFS(depth + 1)
            for r, c in converted: board[r][c] = 0 # 원상 복구
    elif cctv == 5:
        converted = []
        cctv5(0, r0, c0, converted)
        DFS(depth + 1)
        for r, c in converted: board[r][c] = 0 # 원상 복구
    else:
        for dir in range(4):
            converted = [] 
            cctv_direction[cctv](dir, r0, c0, converted)
            DFS(depth + 1)
            for r, c in converted: board[r][c] = 0 # 원상 복구

if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(R) ]
    
    cctvs = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0 or board[r][c] == 6: continue # cctv가 아닌 경우
            cctvs.append((board[r][c], r, c))
    
    answer = 64
    DFS()
    print(answer)