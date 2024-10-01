import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        applicants = [ tuple(map(int, input().split())) for _ in range(N) ]
        applicants.sort()
        
        answer = N # 선발 가능한 인원의 수
        min_n = applicants[0][1]
        
        for i in range(1, N):
            if applicants[i][1] > min_n:
                answer -= 1
            else:
                min_n = applicants[i][1]
                
        print(answer)