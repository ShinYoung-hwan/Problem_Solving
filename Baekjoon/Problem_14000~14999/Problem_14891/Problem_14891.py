import sys
from collections import deque

CLOCKWISE, COUNTERCLOCKWISE = 1, -1
N, S = 0, 1

input = lambda: sys.stdin.readline().rstrip()

def move(start, dir):
    global wheels
    queue = deque()
    visited = [ False ] * 4
    queue.append((start, dir))
    
    while queue:
        cur, dir = queue.popleft()
        left, right = cur-1, cur+1
        
        if 0 <= left and not visited[left] and wheels[left][2] != wheels[cur][6]:
            queue.append((left, -dir))
        if right < 4 and not visited[right] and wheels[cur][2] != wheels[right][6]:
            queue.append((right, -dir))
        
        if dir == CLOCKWISE:
            wheels[cur].appendleft(wheels[cur].pop())
        else:
            wheels[cur].append((wheels[cur].popleft()))
        visited[cur] = True

if __name__ == "__main__":
    wheels = [ deque([int(e) for e in input()]) for _ in range(4) ]
    
    K = int(input())
    for _ in range(K):
        i, dir = map(int, input().split())
        move(i-1, dir)
    
    score = 0
    score += 1 if wheels[0][0] else 0
    score += 2 if wheels[1][0] else 0
    score += 4 if wheels[2][0] else 0
    score += 8 if wheels[3][0] else 0
    print(score)
        