import sys

SIZE = 100_001

input = lambda: sys.stdin.readline().rstrip()

def get_partial_sum(accumulated_sum, s, e):
    # s에서 e까지의 부분 합
    return accumulated_sum[e] - (0 if s == 0 else accumulated_sum[s-1])

def solve(accumulated_sum, n, s):
    # 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성
    res = SIZE
    left, right = 0, 0
    while True:
        if get_partial_sum(accumulated_sum, left, right) >= s:
            res = min(right - left + 1, res)
            left += 1
        else:
            right += 1
            if right >= n: break
        
    return 0 if res == SIZE else res

if __name__ == "__main__":
    n, s = map(int, input().split()) # 수열의 길이 n, 목표 부분 합 s
    sequence = list(map(int, input().split())) # 수열
    
    accumulated_sum = [ sequence[0] ] # i까지의 sequence 축적합
    for i in range(1, n):
        accumulated_sum.append(accumulated_sum[i-1]+sequence[i])
    
    print(solve(accumulated_sum, n, s))