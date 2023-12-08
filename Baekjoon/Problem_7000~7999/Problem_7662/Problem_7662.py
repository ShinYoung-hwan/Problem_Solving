import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

if __name__ == "__main__":
    testcase = int(input())
    
    for _ in range(testcase):
        nOperations = int(input())
        max_heap = list() # 이중 우선순위 큐 / -로 삽입 / 가장 왼쪽에 있는 값이 최댓값
        min_heap = list() # 이중 우선순위 큐 / +로 삽입 / 가장 왼쪽에 있는 값이 최솟값
        nums_dict = dict() # 양쪽 힙 모두 반영하기 위한 딕셔너리
        size = 0 # 이중 우선순위 큐의 크기
        
        for i in range(nOperations):
            line = input().split()
            operation, n = line[0], int(line[1])
            #print(operation, n, end=' ')
            
            if operation == 'I': # 삽입연산
                if n in nums_dict:
                    nums_dict[n] += 1
                else: # 최초 삽입
                    nums_dict[n] = 1                
                    heapq.heappush(min_heap, n)
                    heapq.heappush(max_heap, -n)
                size += 1
                
            else:
                if size != 0:
                    # 힙이 비어있지 않은 경우
                    if n == 1:
                        # 최댓값 삭제
                        while -max_heap[0] not in nums_dict or nums_dict[-max_heap[0]] < 1:
                            # 최댓값 삭제시 동기화 하는 과정 // max_heap에 있는 최댓값이 이미 사라진 경우
                            tmp = -heapq.heappop(max_heap)
                            if tmp in nums_dict:
                                del(nums_dict[tmp])
                        
                        nums_dict[-max_heap[0]] -= 1
                        
                    else: # n == -1
                        # 최솟값 삭제
                        while min_heap[0] not in nums_dict or nums_dict[min_heap[0]] < 1:
                            tmp = heapq.heappop(min_heap)
                            if tmp in nums_dict:
                                del(nums_dict[tmp])
                        nums_dict[min_heap[0]] -= 1
                    size -= 1
                    
            #print(max_heap, min_heap)
            
        # 이중우선순위 큐 출력
        if size == 0:
            print('EMPTY')
        else:
            while -max_heap[0] not in nums_dict or nums_dict[-max_heap[0]] < 1:
                # 최댓값 삭제시 동기화 하는 과정 // max_heap에 있는 최댓값이 이미 사라진 경우
                heapq.heappop(max_heap)
            while min_heap[0] not in nums_dict or nums_dict[min_heap[0]] < 1:
                heapq.heappop(min_heap)
            print(-max_heap[0], min_heap[0])