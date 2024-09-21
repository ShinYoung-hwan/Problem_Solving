import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    K = int(input())
    
    for _ in range(int(input())):
        M, N = map(int, input().split()) # M: 영희, N: 동수
        
        # 양측의 점수가 같은 경우
        if M == N:
            print(1)
        # 영희가 동수보다 고득점인 경우
        elif M > N:
            print(int(2*M - N - K <= 2))
        # 동수가 영희보다 고득점인 경우
        else: # M < N
            print(int(2*N - M - K <= 1))