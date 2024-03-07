import sys

input = lambda: sys.stdin.readline().rstrip()

def solve(features, n):
    res = (sys.maxsize, sys.maxsize, sys.maxsize)
    res_sum = sum(res)
    for fix in range(n-2):
        l = fix + 1
        r = n - 1
        while l < r:
            _sum = features[fix] + features[l] + features[r]
            # 값 최신화
            if abs(_sum) < abs(res_sum):
                res = (features[fix], features[l], features[r])
                res_sum = _sum
                
            # 합계를 높여야함.
            if _sum < 0:
                l += 1
            # 합계를 낮춰야함.
            elif _sum > 0:
                r -= 1
            else:
                return res
    return res

if __name__ == "__main__":
    n = int(input()) # 전체 용액의 수 n
    features = sorted(list(map(int, input().split()))) # n개의 용액의 특성값

    print(*solve(features, n))