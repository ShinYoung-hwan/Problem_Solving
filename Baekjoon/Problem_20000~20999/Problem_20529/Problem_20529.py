import sys
from collections import Counter
from itertools import combinations

input = lambda : sys.stdin.readline().rstrip()

def get_distance(a, b=None, c=None):
    # a, b, c 세사람의 심리적인 거리 구하기
    distance = 0
    
    mbtis = [mbti for mbti in [a, b, c] if mbti is not None]
    
    for m, n in combinations(mbtis, 2):
        for i in range(4):
            if m[i] != n[i]:
                distance += 1
        
    return distance
    
if __name__ == "__main__":
    testcase = int(input())
    
    for _ in range(testcase):
        n = int(input())
        people = input().split()
        mbtis_dict = Counter(people)
        mbtis = mbtis_dict.keys()
        #print(mbtis_dict)
        
        distance = -1
        if len(mbtis) == 1:
            distance = 0
        elif len(people) == 2:
            a, b = people
            distance = get_distance(a, b)
        else:
            if len(people) <= 32:
                for a, b, c in combinations(people, 3):
                    #print(a, b, c)

                    cur_distance = get_distance(a, b, c)
                    distance = cur_distance if distance == -1 else min(distance, cur_distance)  
            else:
                distance = 0                 
            
        print(distance)