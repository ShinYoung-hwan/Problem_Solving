import sys

input = lambda: sys.stdin.readline().rstrip()

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

NOTOUT = 0
REDOUT = 1 
BLUEOUT = 2
BOTHOUT = 3

def movex(rr0, rc0, br0, bc0, direction):
    rr, rc, br, bc = rr0, rc0, br0, bc0
    redout, blueout = 0, 0
    red_first, start, end, step = (rc0 > bc0, 1, C, 1) if direction == RIGHT else (rc0 < bc0, -1, -1, -1)

    if red_first:
        # move red
        for c in range(rc0+start, end, step):
            if board[rr0][c] == '#': break
            if board[rr0][c] == 'O': 
                rr, rc = -1, -1
                redout = REDOUT
                break
            rc = c
        # move blue
        for c in range(bc0+start, end, step):
            if board[br0][c] == '#': break
            if board[br0][c] == 'O': 
                blueout = BLUEOUT
                break
            if br == rr and c == rc: break
            bc = c
    else:
        # move blue
        for c in range(bc0+start, end, step):
            if board[br0][c] == '#': break
            if board[br0][c] == 'O': 
                br, bc = -1, -1
                blueout = BLUEOUT
                break
            bc = c
        # move red
        for c in range(rc0+start, end, step):
            if board[rr0][c] == '#': break
            if board[rr0][c] == 'O': 
                redout = REDOUT
                break
            if rr == br and c == bc: break
            rc = c
    
    return rr, rc, br, bc, redout + blueout

def movey(rr0, rc0, br0, bc0, direction):
    rr, rc, br, bc = rr0, rc0, br0, bc0
    redout, blueout = 0, 0
    
    red_first, start, end, step = (rr0 <= br0, -1, -1, -1) if direction == UP else (rr0 >= br0, 1, R, 1)
    
    if red_first:
        # move red
        for r in range(rr0+start, end, step):
            if board[r][rc0] == '#': break
            if board[r][rc0] == 'O': 
                rr, rc = -1, -1
                redout = REDOUT
                break
            rr = r
        # move blue
        for r in range(br0+start, end, step):
            if board[r][bc0] == '#': break
            if board[r][bc0] == 'O':
                blueout = BLUEOUT
                break
            if bc0 == rc0 and r == rr:
                break
            br = r
    
    else:
        #move blue
        for r in range(br0+start, end, step):
            if board[r][bc0] == '#': break
            if board[r][bc0] == 'O': 
                br, bc = -1, -1
                blueout = BLUEOUT
                break
            br = r
        
        # move red
        for r in range(rr0+start, end, step):
            if board[r][rc0] == '#': break
            if board[r][rc0] == 'O':
                redout = REDOUT
                break
            if rc0 == bc0 and r == br:
                break
            rr = r
            
    return rr, rc, br, bc, redout + blueout

def DFS(rr0, rc0, br0, bc0, depth=1):
    global answer
    if depth > 10:
        return
    
    for direction in range(4):
        rr, rc, br, bc = rr0, rc0, br0, bc0
        is_out = -1
        
        if direction == RIGHT:
            rr, rc, br, bc, is_out = movex(rr0, rc0, br0, bc0, RIGHT)
        elif direction == UP:
            rr, rc, br, bc, is_out = movey(rr0, rc0, br0, bc0, UP)
        elif direction == LEFT:
            rr, rc, br, bc, is_out = movex(rr0, rc0, br0, bc0, LEFT)
        else : # DOWN
            rr, rc, br, bc, is_out = movey(rr0, rc0, br0, bc0, DOWN)
        
        # print(depth, direction, rr, rc, br, bc)
        
        if is_out >= BLUEOUT: continue # prunning
        elif is_out == REDOUT:
            answer = min(answer, depth)
            if depth == 1: return
            continue
        
        DFS(rr, rc, br, bc, depth+1)
    
if __name__ == "__main__":
    R, C = map(int, input().split()) # 세로, 가로
    
    # set board
    board = []
    
    rr, rc = -1, -1
    br, bc = -1, -1
    
    for r in range(R):
        line = [ e for e in input() ]
        
        for c in range(C):
            e = line[c]
            
            if e == 'R':
                rr, rc = r, c
                line[rc] = '.'
            elif e == 'B':
                br, bc = r, c
                line[bc] = '.'
                
        board.append(line)
    
    # solve
    answer = 11
    DFS(rr, rc, br, bc)
    print(-1 if answer == 11 else answer)
    