import sys

input = lambda : sys.stdin.readline().rstrip()

def get_max_height(trees, target_height):
    max_height = 0 # 절단기의 최대 높이
    s, e = 0, max(trees) # 절단기 높이의 시작 / 마지막
    m = (s+e)//2 # 현재 확인하는 절단기 높이
    
    while s <= e:
        diff_height = sum(map(lambda tree: tree-m if tree > m else 0, trees)) # 얻은 나무 길이   

        if diff_height >= target_height: 
            # 얻은 나무가 목표보다 크거나 같음 / 유효 케이스
            s = m+1
            if max_height < m:
                # 
                max_height = m
        else:
            # 얻은 나무가 목표보다 작음 / 무효 케이스
            e = m-1
            
        #print(diff_height, (s,m,e))
        m = (s+e)//2
    
    return max_height

if __name__ == "__main__":
    nTrees, target_height = map(int, input().split())
    trees = list(map(int, input().split()))
    
    print(get_max_height(trees, target_height))
    