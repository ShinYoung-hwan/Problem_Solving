import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    K, N, M = map(int, input().split())
    
    print(max(0, K*N - M))