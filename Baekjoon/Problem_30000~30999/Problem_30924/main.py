import sys
from random import shuffle

input = lambda: sys.stdin.readline().rstrip()

def is_x_n(x: str, n: int):
    print(f"? {x} {n}", flush=True)
    
    is_valid = int(input())
    return bool(is_valid)

if __name__ == "__main__":
    
    ans = []
    for x in ['A', 'B']:
        lst = list(range(1, 10001))
        shuffle(lst)
        
        while True:
            n = lst.pop()
            if not is_x_n(x, n): continue
            
            ans.append(n)
            break
    
    print(f"! {sum(ans)}", flush=True)