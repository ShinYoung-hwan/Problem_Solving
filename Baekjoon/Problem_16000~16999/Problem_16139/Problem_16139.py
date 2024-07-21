import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    S = input() # 문자열
    q = int(input()) # 질문의 수
    
    # set data
    dic = { chr(ord('a') + i): 0 for i in range(26) }
    dp = [ dic ]
    for s in S:
        cur_dic = dp[-1].copy()
        cur_dic[s] += 1
        dp.append(cur_dic)
    
    # solve
    for _ in range(q):
        a, l, r = input().split()
        l, r = int(l), int(r)
        
        print(dp[r+1][a] - dp[l][a])