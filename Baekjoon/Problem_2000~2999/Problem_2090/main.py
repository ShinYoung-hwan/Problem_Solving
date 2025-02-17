import sys, math

input = lambda: sys.stdin.readline().rstrip()

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def __add__(self, others):
        # 통분
        new_denominator = math.lcm(self.denominator, others.denominator)
        
        # 계산
        new_numerator = int(self.numerator * (new_denominator // self.denominator) + others.numerator * (new_denominator // others.denominator))
        
        # 약분
        gcd_num = math.gcd(new_denominator, new_numerator)
        new_denominator //= gcd_num
        new_numerator //= gcd_num
        
        return Fraction(new_numerator, new_denominator)
        
    def inverse(self):
        return Fraction(self.denominator, self.numerator)
    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    harmony = Fraction()
    
    for a in A:
        harmony += Fraction(1, a)
        
    print(harmony.inverse())