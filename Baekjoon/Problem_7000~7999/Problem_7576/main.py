import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

def is_in_warehouse(x, y, x_size, y_size):
    return (0 <= x < x_size) and (0 <= y < y_size)

def get_min_days(warehouse, ripe_tomatoes, size):
    width, depth = size
    min_days = 0
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while len(ripe_tomatoes) != 0:
        tx, ty, min_days = ripe_tomatoes.popleft()
        
        for i in range(4):
            x, y = tx + dx[i], ty + dy[i]
            
            if not is_in_warehouse(x, y, width, depth):
                # 안에 있음
                continue
        
            if warehouse[y][x] == 0:
                ripe_tomatoes.append((x, y, min_days+1))
                warehouse[y][x] = 1
                
    for d in range(depth):
        for w in range(width):
            if warehouse[d][w] == 0:
                return -1
    
    return min_days

if __name__ == "__main__":
    width, depth = map(int, input().split())
    ripe_tomatoes = deque()
    warehouse = list()
    
    for d in range(depth):
        line =  list(map(int, input().split()))
        warehouse.append(line)
        
        for w in range(width):
            if line[w] == 1:
                ripe_tomatoes.append((w, d, 0))
    
    print(get_min_days(warehouse, ripe_tomatoes, (width, depth)))