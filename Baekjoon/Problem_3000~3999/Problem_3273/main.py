import sys

input = lambda: sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    A = sorted(list(map(int, input().split())))
    X = int(input())
    
    answer = 0
    l, r = 0, N-1
    while l < r:
        if A[l] + A[r] == X:
            answer += 1
            l += 1
            r -= 1
        elif A[l] + A[r] > X:
            r -= 1
        else:
            l += 1
    
    print(answer)