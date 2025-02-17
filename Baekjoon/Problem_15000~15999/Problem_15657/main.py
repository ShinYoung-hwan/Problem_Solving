import sys

sys.setrecursionlimit(10**5)

#from itertools import combinations_with_replacement

def combinations_with_replacement(numbers, r, case=[], ans=[]):
    # numbers에서 중복으로 r개를 뽑는 방법

    if len(case) == r:
        ans.append(case)
        return

    for number in numbers:
        if len(case) > 0 and case[-1] > number: continue
        
        case.append(number)
        combinations_with_replacement(numbers, r, case.copy(), ans)
        case.pop()
    
    return ans

input = lambda: sys.stdin.readline().rstrip()
            
if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = sorted([ int(number) for number in input().split() ])
    
    for ai in sorted(combinations_with_replacement(numbers, m)):
        print(*ai)