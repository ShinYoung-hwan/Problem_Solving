import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    N = int(input()) # 구입하고자하는 카트의 장수
    P = list(map(int, input().split())) # i+1장 들어있는 카드팩의 가격 P[i]
    
    max_p = [ 0 ] * (N+1)
    for i in range(1, N+1):
        max_p[i] = P[i-1]
        
        for j in range(i // 2 +1):
            max_p[i] = max(max_p[i], max_p[j] + max_p[i-j])
    
    print(max_p[-1])
    