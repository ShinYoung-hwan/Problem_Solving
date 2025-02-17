import sys

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()
    
def get_min_nCoins(coins, n, target):
    # n종류의 코인들을 이용해 k원을 만드는 최소 동전의 개수 구하기
    nCoins = 0
    for i in range(n):
        nCoin = target // coins[i]
        if nCoin > 0:
            nCoins += nCoin
            target -= coins[i] * nCoin
        
    return nCoins
    
if __name__ == "__main__":
    n, k = map(int, input().split()) # n : 코인의 종류, k : 목표 금액
    coins = [ int(coin.rstrip()) for coin in inputs() ][::-1] # 내림차순으로 정렬된 코인들
    
    print(get_min_nCoins(coins, n, k))