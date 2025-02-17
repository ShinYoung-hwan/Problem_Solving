import sys
from collections import Counter
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

def get_distance(p1, p2):
    # p1와 p2의 심리적인 거리 구하기
    dist = 4
    for i in range(4):
        if p1[i] == p2[i]: dist -= 1
    return dist

def solve(students):
    # 가장 가까운 세 학생 사이의 심리적인 거리 구하기
    mbti_dict = Counter(students)
        
    # 특정 MBTI 3명이 있을 경우
    for v in mbti_dict.values():
        if v >= 3: return 0
    
    # 모든 mbti에 해당하는 사람들이 2명 이하인 경우, 학생 수가 32명 이하인 경우에 해당
    res = 12 # 3 사람의 심리적인 거리
    
    for a, b, c in combinations(students, 3):
        res = min(res, get_distance(a, b) + get_distance(b, c) + get_distance(c, a))
    
    return res
    
if __name__ == "__main__":
    for T in range(int(input())):
        n = int(input()) # 학생의 수
        students = input().split()
        print(solve(students))