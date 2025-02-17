import sys

input = lambda: sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    N = int(input())
    
    print("SK" if N & 1 else "CY")