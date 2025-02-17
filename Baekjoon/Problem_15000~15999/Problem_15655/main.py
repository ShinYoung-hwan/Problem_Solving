import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(start=0, sequence = []):
    # base
    if len(sequence) == M:
        print(*sequence)
        return

    # default
    for i in range(start, N):
        sequence.append(A[i])
        solve(i+1, sequence)
        sequence.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    
    solve()