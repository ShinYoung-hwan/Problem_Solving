import sys

input = lambda: sys.stdin.readline().rstrip()

def matrix_product(A, B, N, M, K):
    C = [ [ 0 ] * K for _ in range(N) ]
    for a in range(N):
        for b in range(K):
            for i in range(M):
                C[a][b] += A[a][i] * B[i][b]
    return C

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [ list(map(int, input().split())) for _ in range(N) ]
    
    M, K = map(int, input().split())
    B = [ list(map(int, input().split())) for _ in range(M) ]
    
    C = matrix_product(A, B, N, M, K)
    
    for row in C:
        print(*row)