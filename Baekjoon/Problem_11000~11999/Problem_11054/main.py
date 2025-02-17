import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(A, n):
    # 길이가 n인 수열 A에서 가장 긴 바이토닉 수열의 길이 구하기
    dp1 = [ 1 ] * n # 크기가 n인 수열 A에서 증가하는 수열의 길이 구하기
    dp2 = [ 1 ] * n # 크기가 n인 수열 A[::-1]에서 증가하는 수열의 길이 구하기
    
    # 크기가 n인 수열 A에서 증가하는 수열의 길이 구하기
    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                dp1[i] = max(dp1[i], dp1[j]+1)
                
    # 크기가 n인 수열 A[::-1]에서 증가하는 수열의 길이 구하기
    A = A[::-1]
    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                dp2[i] = max(dp2[i], dp2[j]+1)
            
    maxdp = [ dp1[i] + dp2[n-1-i] for i in range(n) ]
    
    return max(maxdp) - 1

if __name__ == "__main__":
    n = int(input()) # 수열 A의 크기 n
    A = [ int(e) for e in input().split() ] # 크기가 n인 수열 A
        
    print(solve(A, n))