import sys
sys.set_int_max_str_digits(10 ** 9)

input = lambda: sys.stdin.readline().rstrip()

def pow_div(base, n, r):
    # pow(base, n)을 스마트하게 계산하기
    # 2^4 = 4^2 or 2^8 = 16 ^ 2
    if n == 1: return base % r
    else:
        half = pow_div(base, n//2, r)
        if n % 2 == 0:
            return (half * half) % r
        else:
            return (half * half * base) % r

if __name__ == "__main__":
    a, b, c = map(int, input().split()) # pow(a, b) % c 를 0.5초안에 구하기!
    
    print(pow_div(a, b, c))