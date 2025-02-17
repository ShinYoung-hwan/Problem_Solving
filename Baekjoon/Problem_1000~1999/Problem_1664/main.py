import sys

input = lambda: sys.stdin.readline().rstrip()

def get_primes(n):
    # 에라토스테네스의 체를 이용해서 소수들을 구하기
    primes = []
    eratos = [ True ] * (n+1)
    eratos[1] = False
    for i in range(2, n+1):
        if not eratos[i]: continue
        
        primes.append(i)
        for j in range(i+i, n+1, i):
            eratos[j] = False
        
    return primes

def solve(accumulated_sum, n):
    # 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수
    res = 0
    s, e = 0, 0
    while e < len(accumulated_sum):
        tmp = accumulated_sum[e] - accumulated_sum[s]
        # 목표를 찾은 경우
        if tmp == n:
            res += 1
        
        if tmp > n:
            s += 1
        else:
            e += 1
            
    return res

if __name__ == "__main__":
    n = int(input()) # 자연수 n
    primes = get_primes(n) # 소수들의 리스트
    
    accumulated_sum = [ 0 ] # i번째 소수까지의 축적합
    for i in range(len(primes)):
        accumulated_sum.append(accumulated_sum[i] + primes[i])
    
    print(solve(accumulated_sum, n))