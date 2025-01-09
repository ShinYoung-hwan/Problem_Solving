import sys

input = lambda: sys.stdin.readline().rstrip()

def normalize(num: list[int]) -> None:
    pass
    # num.append(0)
    # for i in range(len(num)-1):
    #     if (num[i] < 0):
    #         borrow = (abs(num[i]) + 9) // 10
    #         num[i+1] -= borrow
    #         num[i] += borrow * 10
    #     else:
    #         num[i+1] += num[i] // 10
    #         num[i] %= 10
            
    # while len(num) > 1 and num[-1] == 0: num.pop()

def multiply(A: list[int], B: list[int]) -> list[int]:
    """ A * B O(NM) """
    C = [ 0 ] * (len(A) + len(B) + 1)
    for i in range(len(A)):
        for j in range(len(B)):
            C[i+j] += A[i] * B[j]
    normalize(C)
    return C

def addTo(A: list[int], B: list[int], k: int) -> None:
    """A += B * 10^k"""
    for i in range(len(B)):
        A[i+k] += B[i]
    normalize(A)
    
def subFrom(A: list[int], B: list[int]) -> None:
    """A -= B"""
    for i in range(len(B)):
        A[i] -= B[i]
    normalize(A)

def karatsuba(A: list[int], B: list[int]) -> list[int]:
    """카라츠바 빠른 곱셈 O(n^log3) ~ O(N^1.58)"""
    """A*B = (A1*10^half + A0) * (B1*10^half + B0) = Z2*10^(2*half) + Z1*10^half + Z0"""
    # base
    if len(A) < len(B): return karatsuba(B, A)
    if len(A) == 0 or len(B) == 0: return []
    if len(A) <= 50: return multiply(A, B)
    
    # default
    # half 구하기
    half = len(A) // 2
    A0, A1 = A[0: half], A[half:]
    B0, B1 = B[0: min(len(B), half)], B[min(len(B), half):]
    
    # Z2 = A1 * B1
    Z2 = karatsuba(A1, B1)
    
    # Z0 = A0 * B0
    Z0 = karatsuba(A0, B0)
    
    # Z1 = (A0 + A1) * (B0 + B1) - Z0 - Z2
    addTo(A0, A1, 0)
    addTo(B0, B1, 0)
    
    Z1 = karatsuba(A0, B0)
    subFrom(Z1, Z0)
    subFrom(Z1, Z2)
    
    ret = []
    addTo(ret, Z0, 0)
    addTo(ret, Z1, half)
    addTo(ret, Z2, half+half)
    
    return ret

def hugs(members: str, fans: str):
    A, B = [] , [] # M(1), F(0)
    for i in range(len(members)): A.append(int(members[i] == 'M'))
    for i in range(len(fans)): B.append(int(fans[i] == 'M'))
    B = B[::-1]
    
    n_hugs = 0
    C = karatsuba(A, B)
    for i in range(len(members)-1, len(fans)):
        if not C[i]: n_hugs += 1
    
    return n_hugs

if __name__ == "__main__":
    C = int(input()) # 테스트케이스의 수
    
    for t in range(C):
        # Male(M), Female(F)
        members = input()
        fans = input()
        print(hugs(members, fans))
            