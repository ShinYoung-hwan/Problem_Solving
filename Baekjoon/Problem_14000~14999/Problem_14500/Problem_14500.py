import sys

from collections import deque
from itertools import combinations

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def is_in(x0, y0):
    global m, n
    return (0 <= x0 < m) and (0 <= y0 < n)

def dfs(x0, y0, rcur_depth, tres, visited):
    global paper, m, n
    
    if rcur_depth == 4:
        return tres
    
    res = tres
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        x, y = x0 + dx[i], y0 + dy[i]
        
        if not is_in(x, y): continue
        if visited[y][x]: continue
        
        visited[y][x] = True
        tmp = dfs(x, y, rcur_depth+1, tres+paper[y][x], visited)
        if tmp > res: res = tmp
        visited[y][x] = False
        
    return res

def get_missing_case(x0, y0):
    global paper, m, n
    res = 0    
    
    missing_cases = [
        ((0, -1), (0, 1), (-1, 0)), # ㅓ
        ((0, -1), (0, 1), (1, 0)),  # ㅏ
        ((0, -1), (-1, 0), (1, 0)), # ㅗ
        ((0, 1), (-1, 0), (1, 0)),  # ㅜ
    ]
    
    for missing_case in missing_cases:
        tmp = paper[y0][x0] # 최초 위치의 값 초기화
        
        i = 0
        while i < 3:
            dx, dy = missing_case[i]
            x, y = x0 + dx, y0 + dy
            if not is_in(x, y): break
            tmp += paper[y][x]
            i += 1
        if i < 3:
            continue
        
        if res < tmp:
            res = tmp            
    
    return res
if __name__ == "__main__":
    n, m = map(int, input().split()) # 가로 m 세로 n 크기의 종이
    paper = [ [ int(num) for num in line.split()  ] for line in inputs() ]
    visited = [ [False] * m for _ in range(n) ]
    res = 0
    
    for y in range(n):
        for x in range(m):
            visited[y][x] = True
            tmp = dfs(x, y, 1, paper[y][x], visited)
            if tmp > res: res = tmp
            tmp = get_missing_case(x, y)
            if tmp > res: res = tmp
            visited[y][x] = False
            
    print(res)