import sys

input = lambda: sys.stdin.readline().rstrip()

N = 9

def is_possible(r, c, v):
    # (r, c) 위치에 v를 채우는 것이 가능한지 확인
    for i in range(N):
        # check row
        if board[r][i] == v: return False
        # check col
        elif board[i][c] == v: return False
    
    # check block
    r0, c0 = 3 * (r // 3), 3 * (c // 3)
    for dr in range(3):
        for dc in range(3):
            r, c = r0 + dr, c0 + dc
            if board[r][c] == v: return False
            
    return True

def solve(depth=0):
    global board
    
    # base case
    if depth == len(blanks):
        return True
    
    # default case
    r, c = blanks[depth]
    for v in range(1, N+1):
        # is possible => check next position
        if not is_possible(r, c, v): continue
        
        board[r][c] = v
        if solve(depth+1): return True
        board[r][c] = 0
    
    return False        

if __name__ == "__main__":
    board = []
    blanks = [] # (r, c) 형식의 빈칸 위치들
    
    # set datas
    for r in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        
        for c in range(N):
            if row[c]: continue
            blanks.append((r, c)) 
    
    # solve
    solve()
    for row in board:
        print(*row)