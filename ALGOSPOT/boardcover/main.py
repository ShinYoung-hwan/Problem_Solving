import sys

input = lambda: sys.stdin.readline().rstrip()
is_in = lambda r, c: (0 <= r < R) and (0 <= c < C)

pieces = [ 
    ((0, 0), (1, 0), (1, 1)), 
    ((0, 0), (0, 1), (1, 0)), 
    ((0, 0), (0, 1), (1, 1)), 
    ((0, 0), (1, 0), (1, -1)),
]

def find_uncovered() -> tuple:
    for r in range(R):
        for c in range(C):
            if is_covered[r][c]: continue
            
            return r, c
    return -1, -1

def is_valid_piece(r0: int, c0: int, piece: tuple[int, int]):
    for dr, dc in piece:
        r, c = r0 + dr, c0 + dc
        
        if not is_in(r, c): return False
        if is_covered[r][c]: return False
        
    return True

def cover(r0: int, c0: int, piece: tuple[int, int], to_blank=False):
    global is_covered
    for dr, dc in piece:
        r, c = r0 + dr, c0 + dc
        is_covered[r][c] = 0 if to_blank else 1

def visit():
    global cnt

    r0, c0 = find_uncovered() # cover할 좌표
    
    # base: cover 완료
    if (r0, c0) == (-1, -1): 
        cnt += 1
        return
    
    # default: cover를 진행해야한다.
    for piece in pieces:
        if not is_valid_piece(r0, c0, piece): continue
        
        cover(r0, c0, piece)
        
        visit()
        
        cover(r0, c0, piece, True)
    
if __name__ == "__main__":
    T = int(input())
    
    for t in range(T):
        # set board info
        R, C = map(int, input().split()) # 보드판의 행(r), 열(c)
        n_empty = 0 # 빈 공간의 수
        is_covered = [] # 벽(1), 빈공간(0)
        
        for r in range(R):
            line = [ 1 if e == '#' else 0 for e in list(input())]
            is_covered.append(line)
            
            for e in line: n_empty += 0 if e else 1

        # found matching count
        cnt = 0
        # 3의 배수가 아닐 경우에만 탐색
        if not n_empty % 3: 
            visit()
        print(cnt)