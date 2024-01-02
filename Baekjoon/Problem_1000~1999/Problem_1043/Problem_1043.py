import sys

input = lambda : sys.stdin.readline().rstrip()

def find(parent, x): # 부모 노드 반환하는 함수
    if x != parent[x]:
        return find(parent, parent[x])
    return x

def union(parent, a, b, truth): # 
    a = find(parent, a)
    b = find(parent, b)
    
    if a in truth and b in truth:
        return
    
    if a in truth: # 진실 판별 능력이 없는 b를 진실 전해들을 수 있는 집단에 삽입
        parent[b] = a
    elif b in truth: # 진십 판별 능력이 없는 a를 진실 전해들을 수 있는 집단에 삽입
        parent[a] = b
    else:
        # truch에 있지 않을 경우 두 원소를 연결, 큰 쪽을 작은 쪽에 연결한다.
        if a < b:
            parent[b] = a
        else:
            parent[a] = b    

if __name__ == "__main__":
    n, m = map(int, input().split()) # n명의 사람, m개의 파티
        
    tmp = list(map(int, input().split()))
    nTruth, truth = tmp[0], set(tmp[1:]) # 진실을 알고 거짓을 잡아내는 사람, 
    
    parties = []
    parent = list(range(n+1))
    for i in range(m):
        # 각 파티 저장
        tmp = list(map(int, input().split()))
        nParty, party = tmp[0], tmp[1:]
        
        for i in range(nParty-1):
            union(parent, party[i], party[i+1], truth)
        
        parties.append(party)
    
    res = 0
    for party in parties:
        for x in party:
            if find(parent, x) in truth:
                break
        else: # for 문 내에서 break가 실행되는 경우 실행 x
            res += 1
            
    print(res)