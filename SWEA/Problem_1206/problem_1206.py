import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(heights, n):
    # n개의 건물의 높이가 heights일 때, 양옆 두칸에 대해 조망권이 확보된 크기 구하기
    res = 0
    
    dx = [-2, -1, 1, 2]
    
    for cur_building in range(n): # n개의 건물에 대한 조망권 구하기
        adjacent_building_heights = []
        
        for i in range(4): # 인접 건물 추가하기
            adjacent_building = cur_building + dx[i]
            if not 0 <= adjacent_building < n: continue
            
            adjacent_building_heights.append(heights[adjacent_building])
        
        viewpoint = heights[cur_building] - max(adjacent_building_heights)
        res += 0 if viewpoint < 0 else viewpoint
    
    return res

if __name__ == "__main__":
    # 10개의 테스트 케이스에 대해 진행
    for T in range(1, 11):
        n = int(input()) # 건물의 개수
        heights = [ int(h) for h in input().split() ] # 각 건물의 높이
        print(f'#{T} {solve(heights, n)}')