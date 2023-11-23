import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

if __name__ == "__main__":
    nOpers = int(input())
    elements = list(map(int, inputs()))
    
    heap = list()
    
    for element in elements:
        if element == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, element)