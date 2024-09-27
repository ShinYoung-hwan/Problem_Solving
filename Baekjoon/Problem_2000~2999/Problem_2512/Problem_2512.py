import sys

input = lambda: sys.stdin.readline().rstrip()

def is_valid(m):
    _sum = 0
    
    for request_budget in request_budgets:
        _sum += ( request_budget if request_budget <= m else m )
    return _sum <= budget

def solve(s, e):
    m = (s + e) // 2 # 가능한 예산
    
    while s <= e:
        if (is_valid(m)):
            s = m+1
        else:
            e = m-1
        m = (s + e) // 2
            
    return m

if __name__ == "__main__":
    N = int(input())
    request_budgets = list(map(int, input().split()))
    budget = int(input())
    
    if sum(request_budgets) <= budget:
        print(max(request_budgets))
    else:
        print(solve(0, max(request_budgets)))