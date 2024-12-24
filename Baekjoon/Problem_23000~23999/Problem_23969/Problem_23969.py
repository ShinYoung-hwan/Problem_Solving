import sys

input = lambda: sys.stdin.readline().rstrip()

def bubble_sort(A, N, K):
    cnt = 0
    for last in range(N, 0, -1):
        for i in range(last-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                cnt += 1
                
                if cnt == K:
                    return A
                
    return [-1]

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    print(*bubble_sort(A, N, K))