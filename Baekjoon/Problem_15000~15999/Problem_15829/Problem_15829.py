import sys

def hashing(string, strlen):
    r, M = 31, 1234567891
    output = 0
    for cnt in range(strlen):
        string_number = ord(string[cnt])-ord('a')+1
        output += string_number * r**cnt
        
    return output % M

if __name__ == "__main__":
    strlen = int(sys.stdin.readline().rstrip())
    string = sys.stdin.readline().rstrip()
    
    print(hashing(string, strlen))