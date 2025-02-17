import sys
input = lambda: sys.stdin.readline().rstrip()

def twopointer(features, n):
    global ans, al, ar
    
    l, r = 0, n - 1
    
    while l < r:
        _sum = features[l] + features[r]
        if abs(_sum) < ans:
            ans = abs(_sum)
            al = l
            ar = r
        
        if _sum == 0:
            break
        
        if _sum > 0:
            r -= 1
        else:
            l += 1
        

def binary_search(features, n, i):
    global ans, al, ar
    
    s, e = i + 1, n - 1
    mid = (s + e) // 2
    
    while s <= e:
        _sum = features[i] + features[mid]
        
        if abs(_sum) < ans:
            ans = abs(_sum)
            al = i
            ar = mid
            
            # 최적해를 찾음
            if _sum == 0:
                break
            
        if _sum >= 0:
            e = mid - 1
        else:
            s = mid + 1
        
        mid = (s + e) // 2
    
if __name__ == "__main__":
    n = int(input()) # 전체 용액의 수
    features = list(map(int, input().split())) # 각 용액의 특성 값, 오름차순으로 정렬되어 있음
    
    # 각 값에 대해서 최솟값을 비교해 최적해를 찾는다. by binary search
    ans = sys.maxsize
    al, ar = 0, n-1
    
    twopointer(features, n)
    
    # for i in range(n-1):
    #     binary_search(features, n, i)
        
    print(features[al], features[ar])