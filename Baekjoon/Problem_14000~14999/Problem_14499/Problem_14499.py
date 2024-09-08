import sys
from collections import deque

EAST, WEST, NORTH, SOUTH = 1, 2, 3, 4

input = lambda: sys.stdin.readline().rstrip()
isIn = lambda r, c: (0 <= r < R) and (0 <= c < C)

dr = [ 0, 0, 0, -1, 1 ]
dc = [ 0, 1, -1, 0, 0 ]

def copy_dice_board(r, c):
    global dice, board
    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0
    if board[r][c]:
        dice[3][1] = board[r][c]
        board[r][c] = 0
    # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
    else:
        board[r][c] = dice[3][1]

def move_east():
    dice[1].appendleft(dice[3][1])
    dice[3][1] = dice[1].pop()
    
def move_west():
    dice[1].append(dice[3][1])
    dice[3][1] = dice[1].popleft()
    
def move_north():
    tmp = dice[0][1]
    dice[0][1] = dice[1][1]
    dice[1][1] = dice[2][1]
    dice[2][1] = dice[3][1]
    dice[3][1] = tmp
    
def move_south():
    tmp = dice[3][1]
    dice[3][1] = dice[2][1]
    dice[2][1] = dice[1][1]
    dice[1][1] = dice[0][1]
    dice[0][1] = tmp

if __name__ == "__main__":
    R, C, r0, c0, K = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(R) ]
    cmds = list(map(int, input().split()))
    
    dice = [ deque([0, 0, 0]) for _ in range(4) ]
    
    for cmd in cmds:
        r, c = r0 + dr[cmd], c0 + dc[cmd]
        if not isIn(r, c): continue # 주사위 굴리기 실패
        
        if cmd == EAST:
            move_east()
        elif cmd == WEST:
            move_west()
        elif cmd == NORTH:
            move_north()
        elif cmd == SOUTH:
            move_south()
        
        copy_dice_board(r, c)
        
        print(dice[1][1])
        r0, c0 = r, c
        