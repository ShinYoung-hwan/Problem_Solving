import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    left = deque(input())
    right = deque()
    
    M = int(input()) # 명령어의 수
    
    for _ in range(M):
        line = input().split()
        cmd = line[0]
        
        if cmd == 'L': # 커서를 왼쪽으로 한칸 이동
            if len(left) == 0: continue
            right.appendleft(left.pop())
        elif cmd == 'D': # 커서를 오른쪽으로 한칸 이동
            if len(right) == 0: continue
            left.append(right.popleft())
        elif cmd == 'B': # 커서 왼쪽에 있는 문자를 삭제한다.
            if len(left) == 0: continue
            left.pop()
        if cmd == 'P': # 커서 왼쪽에 문자를 추가한다.
            e = line[1]
            left.append(e)
        
    print(''.join(left)+''.join(right))