import sys

input = lambda: sys.stdin.readline().rstrip()

def get_row_sum(puzzle, r):
    # row: r인 원소들의 합
    return sum(puzzle[r])

def get_col_sum(puzzle, c):
    # col: c인 원소들의 합
    return sum([ puzzle[r][c] for r in range(len(puzzle)) ])

def get_yx_sum(puzzle):
    # y = x 위치에 있는 원소들의 합
    return sum([ puzzle[i][i] for i in range(len(puzzle)) ])
    ...
def get_y_x_sum(puzzle):
    # y = N - x - 1 위치에 있는 원소들의 합
    N = len(puzzle)
    return sum([ puzzle[N-1-i][i] for i in range(N) ])

def solve(puzzle, N, r0, c0):
    def _is_valid(candidates):
        for i in range(len(candidates)-1):
            if candidates[i] != candidates[i+1]: return False
            
        return True
    
    ans = -1
    candidates = []
    
    for i in range(N):
        if i != r0: 
            candidates.append(get_row_sum(puzzle, i))
        if i != c0:
            candidates.append(get_col_sum(puzzle, i))
    
    # y = x대각선에 존재하지 않는다면
    if r0 != c0:
        candidates.append(get_yx_sum(puzzle))
        
    # y = N - x -1 대각선에 존재하지 않는다면
    if r0 != N - c0 -1:
        candidates.append(get_yx_sum(puzzle))
    
    if _is_valid(candidates):
        new_candidates = []
        new_candidates.append(get_row_sum(puzzle, r0))
        new_candidates.append(get_col_sum(puzzle, c0))
        
        if r0 == c0:
            new_candidates.append(get_yx_sum(puzzle))
        
        if r0 == N - c0 - 1:
            new_candidates.append(get_y_x_sum(puzzle))
        
        if _is_valid(new_candidates):
            ans = candidates[0] - new_candidates[0]
    
    return ans

if __name__ == "__main__":
    N = int(input())
    
    puzzle = list()
    
    r0, c0 = -1, -1 # 비어있는 위치
    
    for r in range(N):
        line = list(map(int, input().split()))
        puzzle.append(line)
        for c in range(N):
            e = line[c]
            
            if e == 0:
                r0, c0 = r, c
    
    if (r0, c0) == (-1, -1):
        print(-1)
    else:
        print(solve(puzzle, N, r0, c0))
            