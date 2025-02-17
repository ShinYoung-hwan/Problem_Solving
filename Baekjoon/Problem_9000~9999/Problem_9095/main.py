import sys

from collections import deque

input = lambda : sys.stdin.readline().rstrip()

def get_cases(n) -> list:
    cases = list()

    queue = deque()
    queue.append([])
    
    while len(queue) > 0:
        cur = queue.popleft()
        sum_cur = sum(cur)
        if sum_cur == n:
            cases.append(cur)
            continue
        
        for i in range(1, 4):
            if sum_cur + i > n:
                break
            cur_cases = cur.copy()
            cur_cases.append(i)
            queue.append(cur_cases)
            
    return cases

nCases = [False] * 12
nCases[0], nCases[1], nCases[2], nCases[3] = 0, 1, 2, 4

def get_nCases(n):
    if n <= 3:
        return nCases[n]
    elif nCases[n] is not False:
        return nCases[n]
    
    cur_nCases = get_nCases(n-1) + get_nCases(n-2) + get_nCases(n-3)
    nCases[n] = cur_nCases
    return cur_nCases

if __name__ == "__main__":
    testcase = int(input())
    
    for _ in range(testcase):
        n = int(input())
        
        print(get_nCases(n))
        
        