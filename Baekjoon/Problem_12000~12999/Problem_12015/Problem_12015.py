import sys

input = lambda: sys.stdin.readline().rstrip()

def binary_search(sequence: list[int], s: int, e: int, target: int) -> int:
    # base
    if s >= e: return s
    
    # default
    m = (s + e) // 2
    if sequence[m] >= target:
        return binary_search(sequence, s, m, target)
    else:
        return binary_search(sequence, m+1, e, target)

def solve(sequence: list[int]):
    lis = []
    
    for e in sequence:
        # 처음 삽인인 경우 or 더 큰 원소가 들어오는 경우
        if not lis or e > lis[-1]:
            lis.append(e)
        # 일반적인 경우 교체한다.
        else:
            index = binary_search(lis, 0, len(lis)-1, e)
            lis[index] = e
    
    return len(lis)

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(A))