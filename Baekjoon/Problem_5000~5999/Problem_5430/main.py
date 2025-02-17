import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

if __name__ == "__main__":
    # 테스트케이스 수
    testcase = int(input())
    
    for _ in range(testcase):
        # 수행할 연산
        operations = input()
        # 정수 배열의 크기
        size = int(input())
        # 배열
        if size == 0: # 입력값 여러개
            numbers =  input()[1:-1].split(',')
        else: 
            numbers = deque([ int(number)for number in  input()[1:-1].split(',')])
        
        is_error = False
        is_queue = True
        for operation in operations:
            if operation == 'D':
                if size == 0:
                    is_error = True
                    break
                else:
                    if is_queue:
                        numbers.popleft()
                    else: # is stack
                        numbers.pop()
                    size -= 1
            else: # operation == 'R':
                is_queue = not is_queue
        
        if is_error:
            print('error')
        else:
            if size == 0:
                print('[]')
            else:
                if not is_queue:
                    numbers.reverse()
                print(str(numbers)[6:-1].replace(' ', ''))