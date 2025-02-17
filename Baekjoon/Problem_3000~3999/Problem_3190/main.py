import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
inBoard = lambda r, c: (0 < r <= N) and (0 < c <= N)
turn = lambda dir, C: (dir + 1) % 4 if C == 'L' else (dir - 1) % 4

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

def get_next_pos(r0, c0, dir):
    r, c = r0, c0
    
    if dir == RIGHT:
        c += 1
    elif dir == UP:
        r -= 1
    elif dir == LEFT:
        c -= 1
    else: # dir == DOWN:
        r += 1
    
    return r, c
    
if __name__ == "__main__":
    N = int(input()) # 보드의 크기 N
    K = int(input()) # 사과의 개수 K
    apples = set([ tuple(map(int, input().split())) for _ in range(K) ]) # { (r, c), ... }

    L = int(input()) # 뱀의 방향변환 횟수 L
    cmds = deque()
    for _ in range(L):
        X, C = input().split()
        cmds.appendleft((int(X), C))
    
    snack = deque([ (1, 1) ])
    snack_pos = { (1, 1) }
    dir = RIGHT
    time = 0
    
    while True:
        # 방향전환
        if len(cmds) and time == cmds[-1][0]:
            _, C = cmds.pop()
            dir = turn(dir, C)
        
        # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        nr, nc = get_next_pos(snack[-1][0], snack[-1][1], dir)
        snack.append((nr, nc))
        
        # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
        if (nr, nc) in snack_pos or not inBoard(nr, nc): break
        
        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if (nr, nc) in apples:
            apples.remove((nr, nc))
        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        else:
            snack_pos.remove(snack[0])
            snack.popleft()
        
        snack_pos.add((nr, nc))
        time += 1

    print(time+1)
    