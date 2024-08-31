import sys

input = lambda: sys.stdin.readline().rstrip()

def get_min_dt(e, s, m):
    min_lst = []
    
    if E - e > 0: min_lst.append(E-e)
    if S - s > 0: min_lst.append(S-s)
    if M - m > 0: min_lst.append(M-m)
    
    return min_lst
    
if __name__ == "__main__":
    E, S, M = map(int, input().split())
    
    e, s, m = 1, 1, 1
    time = 1
    
    while (e, s, m) != (E, S, M):
        dt = min([ 16 - e, 29 - s, 20 - m ])
        dt = min([ dt ] + get_min_dt(e, s, m))
        
        
        e = (e + dt) % 15  if e + dt > 15 else (e + dt)
        s = (s + dt) % 28  if s + dt > 28 else (s + dt)
        m = (m + dt) % 19  if m + dt > 19 else (m + dt)
        
        time += dt
    
    print(time)