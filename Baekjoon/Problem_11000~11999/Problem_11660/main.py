import sys

input = lambda: sys.stdin.readline().rstrip()

def get_square_sum(table, x1, y1, x2, y2):
    # 크기가 n인 table에서 (x1, y1) ~ (x2, y2) 범위 내 합 구하기
    return table[x2][y2] - table[x2][y1-1] - table[x1-1][y2] + table[x1-1][y1-1]

if __name__ == "__main__":
    N, M = map(int, input().split()) # 표의 크기 N, 합을 구해야하는 횟수 M
    
    # NxN 크기의 표 저장
    table = [ [ 0 ] * (N+1) ]
    for _ in range(N):
        row = [ 0 ]
        row.extend(map(int, input().split()))
        table.append(row)
    
    # 표 가로 누적합
    for x in range(1, N+1):
        for y in range(1, N+1):
            table[x][y] += table[x][y-1]
    
    # 표 세로 누적합
    for x in range(1, N+1):
        for y in range(1, N+1):
            table[x][y] += table[x-1][y]
    
    #print(table)
    
    # (x1, y1) - (x2, y2)까지의 합 구하기
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(get_square_sum(table, x1, y1, x2, y2))