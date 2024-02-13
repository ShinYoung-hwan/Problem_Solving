import sys
import math
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def get_chicken_distance(r0, c0, chicken_stores):
    res = math.inf
    for cr, cc in chicken_stores:
        res = min(res, abs(r0 - cr)+abs(c0 - cc))
    return res

if __name__ == "__main__": 
    n, m = map(int, input().split()) # 도시의 크기 (n, n), 최대 치킨집의 수 m
    city = [ [ int(e) for e in line.split() ] for line in inputs() ] # 도시 정보
    
    # 현 치킨집 위치 구하기
    chicken_stores = list()
    houses = list()
    for r in range(n):
        for c in range(n):
            if city[r][c] == 1:
                houses.append((r, c))
            elif city[r][c] == 2:
                chicken_stores.append((r, c))
    
    # 치킨집을 i개씩 발췌해서 각 집에서의 최단 치킨거리구하기
    res = math.inf
    for i in range(1, m+1):
        for filtered_chicken_stores in combinations(chicken_stores, i):
            dist = 0
            for r, c in houses:
                dist += get_chicken_distance(r, c, filtered_chicken_stores)
            res = min(res, dist)
            
    print(res)