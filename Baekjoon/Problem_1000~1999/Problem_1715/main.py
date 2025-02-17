import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    cards = [ int(input()) for _ in range(N) ]
    heapq.heapify(cards)
    
    cnt = 0
    while len(cards) > 1:
        new_card = heapq.heappop(cards) + heapq.heappop(cards)
        cnt += new_card
        heapq.heappush(cards, new_card)
        
    print(cnt)