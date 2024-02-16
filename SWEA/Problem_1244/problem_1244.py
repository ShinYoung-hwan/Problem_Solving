from itertools import combinations
from collections import Counter, deque

def is_more_than_two(number_lst):
    counter = Counter(number_lst)
    for v in counter.values():
        if v >= 2:
            return True
        
    return False

def dfs(number, n, optimized):
    # number를 n회 swap할 때의 최댓값 구하기
    res = 0
    number_str = str(number)
      
    stack = deque()
    stack.append((number, 0))
    
    while stack:
        cur, depth = stack.pop()
        
        # 최적해를 찾음
        if cur == optimized:
            cur_list = list(str(cur))
            if (n - depth) & 1 and not is_more_than_two(cur_list):
                cur_list[-1], cur_list[-2] = cur_list[-2], cur_list[-1]
            res = int(''.join(cur_list))
            break
        
        # dfs 탐색 마침
        if depth == n:        
            res = max(res, cur)
            continue
        
        for i, j in combinations(range(len(number_str)), 2): # 2개씩 swap
            cur_list = list(str(cur))
            cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
            swapped_cur = int(''.join(cur_list))
            
            stack.append((swapped_cur, depth+1))
    
    return res
    
if __name__ == "__main__":
    for T in range(1, int(input()) + 1):
        number, n = map(int, input().split()) # 숫자판의 숫자 number, 교환횟수 n
        
        number_str = str(number)
        number_lst = list(number_str)
        optimized = int(''.join(sorted(number_lst, reverse=True)))
        
        print(f"#{T} {dfs(number, n, optimized)}")