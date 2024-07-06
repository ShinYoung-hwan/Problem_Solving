import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    s = input()
    counter = Counter(s)
    
    print(''.join(sorted(s, key= lambda x: (-counter[x], x))))
