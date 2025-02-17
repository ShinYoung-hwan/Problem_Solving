import sys

input = lambda: sys.stdin.readline().rstrip()

MALE, FEMALE = 1, 2

if __name__ == "__main__":
    N = int(input())
    switches = [ 0 ] + list(map(int, input().split()))
    
    for _ in range(int(input())):
        gender, n = map(int, input().split())
        
        # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
        if gender == MALE:
            for i in range(n, N+1, n):
                switches[i] = int(not switches[i])
        # 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다
        else: # gender == FEMALE
            switches[n] = int(not switches[n])
            for i in range(1, min(n, N-n+1)):
                if switches[n-i] != switches[n+i]: break
                switches[n-i] = int(not switches[n-i])
                switches[n+i] = int(not switches[n+i])
        
    # print
    for i in range(1, N+1):
        print(switches[i], end=' ')
        if i % 20 == 0: print()