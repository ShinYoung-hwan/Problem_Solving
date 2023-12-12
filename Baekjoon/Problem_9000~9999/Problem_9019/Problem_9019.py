import sys
from collections import deque

#sys.setrecursionlimit(10 ** 7)

input = lambda : sys.stdin.readline().rstrip()

def operation_D(number: int) -> int:
    return (2 * number % 10000)
def operation_S(number: int) -> int:
    return ((number - 1) % 10000)
def operation_L(number: int) -> int:
    # d1, d2, d3, d4 -> d2, d3, d4, d1
    return (number // 1000) + (number % 1000) * 10

def operation_R(number: int) -> int:
    # d1, d2, d3, d4 -> d4, d1, d2, d3
    return (number % 10) * 1000 + (number // 10)

def operation(src: int, dest: int) -> str:
    queue = deque([(src, '')]) 
    func_dslr = [(operation_D, 'D'), (operation_S, 'S'), (operation_L, 'L'), (operation_R, 'R')]
    visited = [ False ] * 10000
    visited[src] = True
    
    while True :
        cur, cmd = queue.popleft()
        if cur == dest:
            return cmd
        
        for i in range(4):
            next = func_dslr[i][0](cur)
            if not visited[next]:
                queue.append((next, cmd + func_dslr[i][1]))
                visited[next] = True

if __name__ == "__main__":
    testcase = int(input())
    
    for _ in range(testcase):
        a, b = map(int, input().split())
        
        print(operation(a, b))