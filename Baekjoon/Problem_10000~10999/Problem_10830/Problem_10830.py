import sys

input = lambda: sys.stdin.readline().rstrip()

MOD = 1000

def mat_mul(m1: list, m2: list, N: int):
    # A * B
    new_matrix = [ [0] * N for _ in range(N) ]
    for r in range(N):
        for c in range(N):
            tmp = 0
            for i in range(N):
                tmp += (m1[r][i] * m2[i][c]) % MOD
            new_matrix[r][c] = tmp % MOD
                
    return new_matrix

def mat_pow(matrix: list, N: int, B: int):
    # A ** B를 해결한다.
    # base case
    if B == 1:
        return matrix
    
    # default case
    half = mat_pow(matrix, N, B // 2)
    new_matrix = mat_mul(half, half, N)
    if B & 1:
        new_matrix = mat_mul(new_matrix, matrix, N)
    
    return new_matrix

if __name__ == "__main__":
    N, B = map(int, input().split()) # 행렬의 크기 N, 제곱 B
    
    matrix = [ [ e % MOD for e in map(int, input().split())] for _ in range(N) ]

    for row in mat_pow(matrix, N, B):
        print(*row)
    