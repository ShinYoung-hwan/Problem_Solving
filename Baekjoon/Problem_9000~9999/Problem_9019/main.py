import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solve(A, B):
    # A에서 B로 변환하는 최단 연산 구하기
    visited1 = [ "" ] * 10000
    visited2 = [ "" ] * 10000
    queue = deque()
    queue.append((A, 1))
    queue.append((B, 2))
    
    while queue:
        cur, type = queue.popleft()
        
        if type == 1: # forward
            operations = [
                ((2 * cur) % 10_000, 'D'),
                (9999 if cur == 0 else cur - 1, 'S'),
                (((cur % 1000) * 10 + (cur//1000)), 'L'),
                (((cur % 10) * 1000 + (cur // 10)), 'R'),
            ]
            
            for next, operation in operations:
                if visited1[next] != "" or next == cur: continue # 이미 방문한 숫자인 경우
                
                queue.append((next, type))
                visited1[next] = ''.join((visited1[cur], operation))
                
                if next == B: return visited1[next]
                elif visited1[next] != "" and visited2[next] != "":
                    return ''.join((visited1[next], visited2[next]))

        else: # backward
            operations = [
                (cur // 2, 'D'), # not mod operation case
                ((cur + 10000) // 2, 'D'), # mod operation case
                (0 if cur == 9999 else cur + 1, 'S'),
                (((cur % 10) * 1000 + (cur // 10)), 'L'),
                (((cur % 1000) * 10 + (cur//1000)), 'R'),
            ]
            
            for next, operation in operations:
                if visited2[next] != "" or next == cur: continue # 이미 방문한 숫자인 경우
                if operation == "D" and cur % 2 != 0: continue # 2로 나누어 떨어지지 않아 구할 수 없는 경우
                
                queue.append((next, type))
                visited2[next] = ''.join((operation, visited2[cur]))
                
                if next == A: return visited2[next]
                elif visited1[next] != "" and visited2[next] != "":
                    return ''.join((visited1[next], visited2[next]))
            
if __name__ == "__main__":

    for T in range(int(input())):
        A, B = map(int, input().split()) # 초기값 A, 최종값 B

        print(solve(A, B))