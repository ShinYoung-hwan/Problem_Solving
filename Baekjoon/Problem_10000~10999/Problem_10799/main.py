import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    line = input() # 쇠막대기의 배치
    
    stack = 0
    cnt = 0
    for idx in range(len(line)):
        # '(' cmd
        if line[idx] == '(':
            stack += 1
        else:
            stack -= 1
            cnt += stack if line[idx-1] == '(' else 1
            
    print(cnt)