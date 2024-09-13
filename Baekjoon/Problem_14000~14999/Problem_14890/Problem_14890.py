import sys

input = lambda: sys.stdin.readline().rstrip()

def check_row(r):
    global answer
    def is_valid_front(c):
        cnt = 1
        height = heights[r][c]
        for i in range(c-1, -1, -1):
            if cnt == L: return True
            if heights[r][i] != height: break
            cnt += 1
        return cnt == L
    def is_valid_back(c):
        cnt = 1
        height = heights[r][c]
        for i in range(c+1, N):
            if cnt == L: return True
            if heights[r][i] != height: break
            cnt += 1
        height = heights[r][c]
        return cnt == L
    
    climed = [ False ] * N # 경사면을 설치했는지에 대해
    
    for c in range(1, N):
        # 높이가 같은 경우
        if heights[r][c-1] == heights[r][c]: continue
        
        # 높이차가 2 이상인 경우
        if abs(heights[r][c-1] - heights[r][c]) >= 2: return
        
        # 높이차가 1인 경우
        # 오름
        if heights[r][c-1] < heights[r][c]:
            if not is_valid_front(c-1): return
            for i in range(c-1, c-1-L, -1):
                if climed[i]: return
                climed[i] = True
        # 내림
        else: # heights[r][c-1] > heights[r][c]
            if not is_valid_back(c): return
            for i in range(c, c+L):
                if climed[i]: return
                climed[i] = True
    
    answer += 1
    # print("row", r)
    
def check_col(c):
    global answer
    def is_valid_front(r):
        cnt = 1
        height = heights[r][c]
        for i in range(r-1, -1, -1):
            if cnt == L: return True
            if heights[i][c] != height: break
            cnt += 1
        return cnt == L
    def is_valid_back(r):
        cnt = 1
        height = heights[r][c]
        for i in range(r+1, N):
            if cnt == L: return True
            if heights[i][c] != height: break
            cnt += 1
        return cnt == L
    
    climed = [ False ] * N # 경사면을 설치했는지에 대해
    
    for r in range(1, N):
        # 높이가 같은 경우
        if heights[r-1][c] == heights[r][c]: continue
        
        # 높이차가 2 이상인 경우
        if abs(heights[r-1][c] - heights[r][c]) >= 2: return
        
        # 높이차가 1인 경우
        # 오름
        if heights[r-1][c] < heights[r][c]:
            if not is_valid_front(r-1): return
            for i in range(r-1, r-1-L, -1):
                if climed[i]: return
                climed[i] = True
        # 내림
        else:
            if not is_valid_back(r): return
            for i in range(r, r+L):
                if climed[i]: return
                climed[i] = True
    
    answer += 1
    # print("col", c)

if __name__ == "__main__":
    N, L = map(int, input().split())
    heights = [ list(map(int, input().split())) for _ in range(N) ]
    
    answer = 0
    for i in range(N):
        check_row(i)
        check_col(i)
    
    print(answer)