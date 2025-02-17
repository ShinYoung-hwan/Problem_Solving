import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

if __name__ == "__main__":
    n, m = map(int, input().split()) # n개의 수에 대해 m가지 경우의 결과 구하기
    numbers = [ int(number) for number in input().split() ] # n개의 정수
    
    accumulated_sum = [ 0 ]
    for i in range(0, n):
        accumulated_sum.append(accumulated_sum[i] + numbers[i])
    
    for _ in range(m):
        i, j = map(int, input().split()) # i부터 m까지의 합
        print(accumulated_sum[j]- accumulated_sum[i-1])