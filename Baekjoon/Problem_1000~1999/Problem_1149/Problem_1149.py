import sys

input = lambda : sys.stdin.readline().rstrip()  
    
if __name__ == "__main__":
    n = int(input()) # n개의 집
    
    houses = list() # 집들의 색칠 cost
    for _ in range(n):
        r, g, b = map(int, input().split()) # 각 집을 r, g, b 중 하나로 색칠할 때 해당 색깔의 cost
        house = [0, 0, 0]
        house[0], house[1], house[2] = r, g, b # (0:R), (1:G), (2:B)
        houses.append(house)
    
    res = [[houses[0][0], houses[0][1], houses[0][2]]] # 0에서 R, G, B를 선택했을 때의 값.
    for i in range(1, n):
        minimun = list()
        minimun.append(min(res[i-1][1]+houses[i][0], res[i-1][2]+houses[i][0])) # i번째에서 R을 선택할 때
        minimun.append(min(res[i-1][0]+houses[i][1], res[i-1][2]+houses[i][1])) # i번째에서 G을 선택할 때
        minimun.append(min(res[i-1][0]+houses[i][2], res[i-1][1]+houses[i][2])) # i번째에서 B을 선택할 때
        res.append(minimun)
        
    print(min(res[-1]))
    