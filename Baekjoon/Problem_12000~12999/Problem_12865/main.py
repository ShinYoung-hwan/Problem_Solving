import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(stuffs, n, k):
    # k 무게까지 담을 수 있는 배낭에 넣을 수 있는 물건들의 가치의 최댓값
    
    dp = [ [0] * (n+1) for _ in range(k+1) ] # dp[w][i]: 무게가 w인 가방에서 i번째 물건까지 고려했을 때 최대 가지
    
    # print(dp)
    
    for i in range(1, n+1):
        wi, vi = stuffs[i]
        for w in range(1, k+1):
            if wi <= w:
                dp[w][i] = max(dp[w][i-1], dp[w-wi][i-1] + vi)
            else:
                dp[w][i] = dp[w][i-1]
    
    return dp[k][n]
    
if __name__ == "__main__":
    n, k = map(int, input().split()) # 물품의 수 n, 담을 수 있는 무게 k
    
    stuffs = [ (0, 0) ]
    for _ in range(n):
        w, v = map(int, input().split()) # 무게 w, 가치 v
        stuffs.append((w, v))
        
    print(solve(stuffs, n, k))