import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, K = map(int, input().split())
    
    score_dict = dict()
    prev = (0, 2e+7, 2e+7, 2e+7)
    for i, score in enumerate(sorted([ list(map(int, input().split())) for _ in range(N) ], key=lambda x: (-x[1], -x[2], -x[3]))):
        id = score[0]
        
        # 메달이 다른 경우에만 update
        if prev[1:] != score[1:]:
            prev = score
            prev[0] = i
        
        # 순위 기록
        score_dict[id] = prev[0]+1
    
    print(score_dict[K])
    