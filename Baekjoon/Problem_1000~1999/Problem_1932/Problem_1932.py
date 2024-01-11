import sys

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def solve(triangle, n):
    # 높이가 n인 삼각형을 1부터 n까지 탐색할 때 최댓값을 구하기
    dist = [ [0] * i for i in range(1, n+1) ]

    dist[0][0] = triangle[0][0]
    for h in range(1, n):
        for w in range(h+1):
            if w == 0:
                dist[h][w] = dist[h-1][w] + triangle[h][w]
            elif w == h:
                dist[h][w] = dist[h-1][w-1] + triangle[h][w]
            else: # 경로가 2개인 경우
                dist[h][w] = max(dist[h-1][w] + triangle[h][w], dist[h-1][w-1] + triangle[h][w])
    
    return max(dist[-1])

if __name__ == "__main__":
    n = int(input()) # 삼각형의 높이
    
    triangle = [ [ int(e) for e in h.rstrip().split() ] for h in inputs() ]
    print(solve(triangle, n))