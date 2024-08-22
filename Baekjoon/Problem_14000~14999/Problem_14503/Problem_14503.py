import sys

input = lambda: sys.stdin.readline().rstrip()
turn_cclockwise_90 = lambda d: (d-1)%4

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

def is_near_clear(isClear, r, c):
    if not isClear[r-1][c]: return False
    elif not isClear[r][c-1]: return False
    elif not isClear[r+1][c]: return False
    elif not isClear[r][c+1]: return False
    
    return True

def get_position(r0, c0, d, front: bool):
    r, c = r0, c0
    dr, dc = (1, 1) if front else (-1, -1)
    if d == NORTH:
        r -= dr
    elif d == EAST:
        c += dc
    elif d == SOUTH:
        r += dr
    elif d == WEST:
        c -= dc

    return r, c

def solve(r0, c0, d):
    isClear = [ [ True if isWall[r][c] else False for c in range(C) ] for r in range(R) ]
    cnt = 0
    
    while True:
        if not isClear[r0][c0]: 
            isClear[r0][c0] = True
            cnt += 1
        
        # 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
        if is_near_clear(isClear, r0, c0):
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            r, c = get_position(r0, c0, d, False)
            if not isWall[r][c]: 
                r0, c0 = r, c
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
        # 현재 칸의 주변 4 중 청소되지 않은 빈 칸이 있는 경우,
        else:
            # 반시계 방향으로 90도 회전한다.
            d = turn_cclockwise_90(d)
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            r, c = get_position(r0, c0, d, True)
            if not isWall[r][c] and not isClear[r][c]:
                r0, c0 = r, c
            # 1번으로 돌아간다.
            
    return cnt

if __name__ == "__main__":
    R, C = map(int, input().split())
    r0, c0, d = map(int, input().split())
    isWall = [ list(map(int, input().split())) for _ in range(R) ]
    
    print(solve(r0, c0, d))