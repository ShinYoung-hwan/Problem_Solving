def Pectorial(n):
    output = 1
    for i in range(1, n+1): output = output * i
    return output

def Permutation(n, r):
    output = 1
    for i in range(n - r, n + 1): output = output * i
    return output

def Combination(n, r):
    return Permutation(n, r) / Pectorial(r)

def main():
    Testcase = int(input())

    for i in range(Testcase):
        N = int(input())
        M = int(input())

        print(Combination(M, N))

main()