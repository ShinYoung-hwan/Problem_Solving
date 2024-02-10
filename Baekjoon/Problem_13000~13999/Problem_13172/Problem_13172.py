import sys

MOD = 1_000_000_007

input = lambda: sys.stdin.readline().rstrip()

def pow(base, exp, mod):
    # 분할정복을 이용한 제곱
    if exp == 1:
        return base % mod
    half = pow(base, exp//2, mod) 
    if exp & 1: # 홀수
        return (half * half * base) % mod
    else: # 짝수
        return (half * half) % mod

if __name__ == "__main__": 
    m = int(input()) # 주사위의 수
    
    means = []
    for i in range(m):
        ni, si = map(int, input().split()) # i번째 주사위는 ni면체 주사위 and 주사위의 눈 총합이 si
        # ni의 역원 이용하기
        inverse_ni = pow(ni, MOD-2, MOD)
        means.append(si * inverse_ni % MOD)
    
    # 역원을 이용한 기댓값들의 기댓값구하기
    mean = 0
    for i in range(m):
        mean = (mean + means[i]) % MOD
    
    print(mean)
