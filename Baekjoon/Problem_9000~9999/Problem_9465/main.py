import sys

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def solve(stickers, n):
    # (2,n) 크기의 스티커들로부터 최대 값 구하기
    if n == 1: return max(stickers[0][0], stickers[1][0])
    
    dist = [ [ 0 ] * n for _ in range(2) ]
    dist[0][0] = stickers[0][0]
    dist[1][0] = stickers[1][0]
    dist[0][1] = dist[1][0] + stickers[0][1]
    dist[1][1] = dist[0][0] + stickers[1][1]
    
    for i in range(2, n):
        dist[0][i] = max(dist[1][i-1], dist[0][i-2], dist[1][i-2]) + stickers[0][i]
        dist[1][i] = max(dist[0][i-1], dist[0][i-2], dist[1][i-2]) + stickers[1][i]
    
    #print(dist[0])
    #print(dist[1])
        
    return max(dist[0][-1], dist[1][-1])

if __name__ == "__main__":
    for T in range(int(input())):
        n = int(input()) # 각 행의 스티커의 수
        stickers = []
        stickers.append([ int(e) for e in input().split() ]) # 1행
        stickers.append([ int(e) for e in input().split() ]) # 2행
        
        #print(stickers[0])
        #print(stickers[1])
        
        print(solve(stickers, n))