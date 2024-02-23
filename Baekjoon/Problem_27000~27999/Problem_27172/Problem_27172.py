import sys

SIZE = 1_000_001

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    n = int(input()) # 플레이서의 수 n
    x = list(map(int, input().split()))  # 각 플레이어가 갖고 있는 카드 x[i]
    
    in_hands = [ -1 for _ in range(SIZE) ] # i카드가 누구한테 있는지...
    for i in range(n):
        in_hands[x[i]] = i
    
    scores = [ 0 ] * (n) # 각 플레이어의 점수
    for i in range(n): # i 번째 사람을 기준으로 계산
        for j in range(2*x[i], SIZE, x[i]): # i 번째 사람과 상대하는 사람
            if in_hands[j] == -1: continue
            
            scores[i] += 1
            scores[in_hands[j]] -= 1
            
    print(*scores)