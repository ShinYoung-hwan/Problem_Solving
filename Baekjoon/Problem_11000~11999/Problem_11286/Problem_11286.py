import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()
    
if __name__ == "__main__":
    n = int(input())
    operations = [ int(operation) for operation in inputs() ]
    
    hq = list()
    
    for operation in operations:
        if operation == 0:
            if len(hq) == 0:
                print(0)
            else:
                priority, value = heapq.heappop(hq)
                print(value)
        else:
            heapq.heappush(hq, (abs(operation), operation))
    