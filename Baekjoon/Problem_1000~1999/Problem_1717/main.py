import sys

input = lambda: sys.stdin.readline().rstrip()

def find(parent, a):
    """ 재귀로 작성시 recursion error 발생 가능 """
    a0 = a
    while parent[a] != a:
        a = parent[a]
    parent[a0] = a
    return a

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    # 작은 것이 위로 가게
    if (a >= b): parent[a] = b
    else: parent[b] = a

if __name__ == "__main__":
    n, m = map(int, input().split()) # 집합의 개수 n, 연산의 개수 m
    parent = [ i for i in range(n+1) ]
    
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        
        # a가 있는 원소와 b가 있는 원소를 결합
        if cmd == 0:
            union(parent, a, b)
        # a와 b가 갗은 집합에 존재
        elif cmd == 1:
            print("YES" if find(parent, a) == find(parent, b) else "NO")