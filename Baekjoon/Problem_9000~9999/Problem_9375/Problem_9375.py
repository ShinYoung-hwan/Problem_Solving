import sys

input = lambda : sys.stdin.readline().rstrip()
inputs = lambda : sys.stdin.readlines()

def get_clothes(nClothes):
    clothes = dict()
    
    for _ in range(nClothes):
        cloth, type = input().split()
        
        if type in clothes:
            clothes[type].append(cloth)
        else: # type not in clothes
            clothes[type] = [ cloth ]
        
    return clothes

def get_nCase(clothes: dict):
    nCase = 1
    
    for v in clothes.values():
        nCase *= len(v) + 1
    
    return nCase - 1

if __name__ == "__main__":
    
    for _ in range(int(input())):
        nClothes = int(input())
        clothes = get_clothes(nClothes)
        
        print(get_nCase(clothes))
        
        