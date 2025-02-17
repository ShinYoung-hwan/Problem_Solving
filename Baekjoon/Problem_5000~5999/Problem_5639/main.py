import sys
sys.setrecursionlimit(10**5)

inputs = lambda: sys.stdin.readlines()

def postorder(preorder, s, e):
    # CLR -> LRC
    if s > e: return
    
    mid = e + 1 # 오른쪽 서브트리가 없는 경우
    
    for i in range(s+1, e+1):
        if preorder[s] < preorder[i]: # R로 파고들어야하는 경우
            mid = i
            break

    postorder(preorder, s+1, mid-1) # 왼쪽 서브트리
    postorder(preorder, mid, e)     # 오른족 서브트리
    print(preorder[s])              # 루트 노드

if __name__ == "__main__":
    preorder = [ int(node.rstrip()) for node in inputs() ] # 전위 순회로 주어진 이진 검색 트피
    
    postorder(preorder, 0, len(preorder) - 1)