import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

if __name__ == "__main__":
    n = int(input())
    numbers = [ int(number) for number in inputs() ]
    hq = []
    
    for number in numbers:
        if number == 0:
            if len(hq) == 0:
                print(0)
            else:
                priority, element = heapq.heappop(hq)
                print(element)
        else:
            heapq.heappush(hq, (-number, number))