import sys

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def get_air_purifier(house, R):
    for r in range(R):
        if house[r][0] == -1:
            return r, 0
        
def spread_fine_dust(house, R, C):
    # 각 위치에서 미세먼지 확산
    after_spread_dust_house = [ [ 0 ] * C for _ in range(R) ]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for r0 in range(R):
        for c0 in range(C):
            if house[r0][c0] == 0: continue # 미세먼지가 없는 경우
            if house[r0][c0] == -1: # 공기청정기가 설치된 경우
                after_spread_dust_house[r0][c0] = -1
                continue 
            
            nPath = 0 # 확산 방향 수
            nSpread = house[r0][c0] // 5 # 확산량
            
            for i in range(4):
                r, c = r0 + dr[i], c0 + dc[i]
                if not((0 <= r < R) and (0 <= c < C)): continue
                if house[r][c] == -1: continue
                nPath += 1
                after_spread_dust_house[r][c] += nSpread
            after_spread_dust_house[r0][c0] += house[r0][c0] - nSpread * nPath
            
    return after_spread_dust_house
    
def run_air_purifier(house, R, C, ar0, ac0):
    # (ar0, ac0)에서 상단으로, (ar0+1, ac0)에서 하단으로 순환하는 청정기 작동
    # (ar0, ac0)에서 청정기 작동
    
    # 상
    for ar in range(ar0-1, 0, -1):
        house[ar][0] = house[ar-1][ac0]
    # 우
    for ac in range(C-1):
        house[0][ac] = house[0][ac+1]
    # 하
    for ar in range(ar0):
        house[ar][C-1] = house[ar+1][C-1]
    # 좌
    for ac in range(C-1, 1, -1):
        house[ar0][ac] = house[ar0][ac-1]
    house[ar0][1] = 0
    # (ar0+1, ac0)에서 청정기 작동
    ar0 = ar0 + 1
    # 하
    for ar in range(ar0+1, R-1):
        house[ar][0] = house[ar+1][0]
    # 우
    for ac in range(C-1):
        house[R-1][ac] = house[R-1][ac+1]
    # 상
    for ar in range(R-1, ar0, -1):
        house[ar][C-1] = house[ar-1][C-1]
    # 좌
    for ac in range(C-1, 1, -1):
        house[ar0][ac] = house[ar0][ac-1]
    house[ar0][ac0+1] = 0
        
def solve(house, R, C, T):
    # 크기가 (R, C)인 집에서 T초 동안 미세먼지 확산 & 공기청정기 작동
    ar, ac = get_air_purifier(house, R) # 공기청정기 위치
    
    for _ in range(T):
        # 미세먼지 확산
        house = spread_fine_dust(house, R, C)
        # for row in house:
        #     print(row)
        # print()
        
        # 공기청정기 작동
        run_air_purifier(house, R, C, ar, ac)
        # for row in house:
        #     print(row)
        # print()
    
    # T초후 house의 총 미세먼지
    res = 2 # 공기청정기 2칸 고려
    for row in house:
        res += sum(row)
    return res

if __name__ == "__main__": 
    R, C, T = map(int, input().split()) # 집의 크기 (R, C), 경과 시간 T
    house = [ [ int(e) for e in row.split() ] for row in inputs() ] # 집 내 미세먼지 정보

    print(solve(house, R, C, T))
    