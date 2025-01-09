#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
const int SIZE = 200001;

void normalize(vector<int> &A) {
    return;
}

vector<int> multiply(const vector<int> &A, const vector<int> &B) {
    vector<int> C(A.size() + B.size() + 1, 0);
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < B.size(); j++) {
            C[i+j] += A[i] * B[j];
        }
    }
    normalize(C);
    return C;
}

void add_to(vector<int> &A, const vector<int> &B, const int k) {
    if(A.size() < B.size() + k)
		A.resize(B.size() + k);
    for (int i = 0; i < B.size(); i++) {
        A[k+i] += B[i];
    }
    normalize(A);
}

void sub_from(vector<int> &A, const vector<int> &B) {
    for (int i = 0; i < B.size(); i++) {
        A[i] -= B[i];
    }
    normalize(A);
}

vector<int> karatsuba(const vector<int> &A, const vector<int> &B) {
    /* 카라츠바 빠른 곱셈 O(n^1.58) */
    // base
    if (A.size() < B.size()) return karatsuba(B, A);
    if (A.empty() || B.empty()) return {};
    if (A.size() <= 50) return multiply(A, B);

    // default
    /* let a = a1 * 10 ^ k + a0, b = b1 * 10 ^ k + b0
     * z = a * b 
     * = a1b1 * 10 ^ 2k + (a1b0 + a0b1) * 10 ^ k + a0b0
     * let z2 = a1b1, z0 = a0b0
     * z1 = (a1+a0) * (b1+b0) - z2 - z0 
     */ 
    int half = A.size() / 2;
    vector<int> a0 = vector<int>(A.begin(), A.begin()+half), \
                a1 = vector<int>(A.begin()+half, A.end());
    vector<int> b0 = vector<int>(B.begin(), B.begin()+min<int>(half, B.size())), \
                b1 = vector<int>(B.begin()+min<int>(half, B.size()), B.end());

    vector<int> z2 = karatsuba(a1, b1);
    vector<int> z0 = karatsuba(a0, b0);

    add_to(a0, a1, 0);
    add_to(b0, b1, 0);
    vector<int> z1 = karatsuba(a0, b0);

    sub_from(z1, z2);
    sub_from(z1, z0);

    vector<int> ret;
    add_to(ret, z0, 0);
    add_to(ret, z1, half);
    add_to(ret, z2, half+half);

    return ret;
}

int hugs(const string &members, const string &fans) {
    vector<int> A, B;
    for (int i = 0; i < members.size(); i++) A.push_back(members[i] == 'M');
    for (int i = 0; i < fans.size(); i++) B.push_back(fans[i] == 'M');
    reverse(B.begin(), B.end());

    vector<int> C = karatsuba(A, B);
    int n_hugs = 0;
    for (int i = A.size()-1; i < B.size(); i++) {
        if (C[i] == 0) n_hugs += 1;
    }

    return n_hugs;
}

int main(int argc, char **argv) {
    int C; scanf("%d", &C);

    for (int t = 0; t < C; t++) {
        char members[SIZE], fans[SIZE]; scanf("%s %s", members, fans);
        printf("%d\n", hugs(members, fans));
    }

    return 0;
}