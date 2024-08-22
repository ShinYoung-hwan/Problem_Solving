import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input()) # 로프의 개수
    ropes = sorted([ int(input()) for _ in range(N) ], reverse=True)
    
    answer = 0
    for i in range(N):
        answer = max(answer, ropes[i] * (i+1))
    print(answer)