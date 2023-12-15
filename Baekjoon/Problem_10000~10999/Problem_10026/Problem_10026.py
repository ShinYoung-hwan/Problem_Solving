import sys

from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def is_in_image(w, h, n):
    return (0 <= w < n) and (0 <= h < n)

def bfs(image, n, visited, start):
    queue = deque([start])
    visited[start[1]][start[0]] = True
    
    dw = [1, 0, -1, 0]
    dh = [0, 1, 0, -1]
    
    while len(queue) > 0:
        tw, th = queue.popleft()
        
        for i in range(4):
            w, h = tw + dw[i], th + dh[i]
            
            if not is_in_image(w, h, n):
                continue
            elif visited[h][w]:
                continue
            
            if image[h][w] == image[start[1]][start[0]]:
                queue.append((w, h))
                visited[h][w] = True
    
    return visited

def get_nZones(image, n, is_color_blindness):
    nZones = 0
    if is_color_blindness:
        image = [ [ 'B' if pixel == 'B' else 'R' for pixel in line ]  for line in image ]
    visited = [[False] * n for _ in range(n)]
    
    for h in range(n):
        for w in range(n):
            if visited[h][w]:
                continue
            
            visited = bfs(image, n, visited, (w, h))
            nZones += 1
    
    return nZones

if __name__ == "__main__":
    n = int(input())
    image = [ list(line.rstrip()) for line in inputs() ]
    
    print(get_nZones(image, n, False), get_nZones(image, n, True))