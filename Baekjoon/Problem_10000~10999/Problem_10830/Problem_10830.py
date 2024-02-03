import sys
sys.setrecursionlimit(10*9)

input = lambda: sys.stdin.readline().rstrip()
inputs = lambda: sys.stdin.readlines()

def multiply_matrix(A, B, n):
    # 크기가 nxn인 두 행렬 A, B의 곱 구하기
    res = [ [ 0 ] * n for _ in range(n) ]
    
    for row in range(n):
        for col in range(n):
            tmp = 0
            for i in range(n):
                tmp += A[row][i] * B[i][col]
            res[row][col] = tmp % 1000 # 1,000으로 나눈 나머지를 저장. 
            
    return res

def solve(A, n, b):
    # 분할정복을 이용해서 제곱을 두 절반 행렬의 곱으로 구한다.
    if b == 1:
        return A
    elif b % 2 == 0: # 짝수
        half = solve(A, n, b//2)
        return multiply_matrix(half, half, n)
    else: # 홀수
        b = b - 1
        half = solve(A, n, b//2)
        return multiply_matrix(multiply_matrix(half, half, n), A, n)

if __name__ == "__main__":
    n, b = map(int, input().split()) # nxn 크기의 행렬 A, a^b를 구할 계획
    
    A = [ [ int(e) for e in line.split() ] for line in inputs() ]
    
    for ai in solve(A, n, b):
        for aij in ai:
            print(aij % 1000, end=' ')
        print()