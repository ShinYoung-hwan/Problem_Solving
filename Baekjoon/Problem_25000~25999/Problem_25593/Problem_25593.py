import sys

input = lambda: sys.stdin.readline().rstrip() 

def update_table(table: dict, name: str, time: int):
    if name == "-": return
    
    if name in table:
        table[name] += time
    else:
        table[name] = time

if __name__ == "__main__":
    N = int(input()) # 주의 개수
    
    table = dict()
    
    for _ in range(N): # 각 주에 대해 실행
        for i in range(4): # 근무 시간대
            names = input().split()
            time = 0
            if i == 0: # 08:00~12:00(4)
                time = 4
            elif i == 1: # 12:00~18:00(6)
                time = 6
            elif i == 2: # 18:00~22:00(4)
                time = 4
            else: # i == 3 # 22:00~08:00(10)
                time = 10
            
            for name in names:
                update_table(table, name, time)
    
    if not table:
        print("Yes")
    else:
        values = table.values()
        diff = max(values) - min(values)
        print("Yes" if diff <= 12 else "No")
            