import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def is_in_warehouse(x, y, z, w, d, h):
    return (0 <= x < w) and (0 <= y < d) and (0 <= z < h)

def get_min_days(warehouse, ripe_tomatoes, size):
    width, depth, height = size
    min_days = 0
    
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    
    while len(ripe_tomatoes) != 0:
        tx, ty, tz, min_days = ripe_tomatoes.popleft()
        
        for i in range(6):
            x, y, z = tx+dx[i], ty+dy[i], tz+dz[i]
            
            if not is_in_warehouse(x, y, z, width, depth, height):
                # 창고 범위 밖이면 다음 위치 확인
                continue
            
            if warehouse[z][y][x] == 0:
                # 아직 안익은 경우
                warehouse[z][y][x] = 1
                ripe_tomatoes.append((x, y, z, min_days+1))
                
    # 익히기 과정이 완료된 후에도 안익은 토마토가 있는 경우, -1 반환
    for h in range(height):
        for d in range(depth):
            for w in range(width):
                if warehouse[h][d][w] == 0:
                    return -1                
    
    return min_days

if __name__ == "__main__":
    width, depth, height = map(int, input().split())
    warehouse = [ list() for _ in range(height) ]
    ripe_tomatoes = deque()
    
    # 토마토 창고 저장
    for h in range(height):
        for d in range(depth):
            warehouse[h].append([ int(line) for line in input().split() ])
            
            for w in range(width):
                if warehouse[h][d][w] == 1:
                    ripe_tomatoes.append((w, d, h, 0))
        

    print(get_min_days(warehouse, ripe_tomatoes, (width, depth, height)))