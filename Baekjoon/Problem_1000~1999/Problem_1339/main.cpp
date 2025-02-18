#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
const int SIZE = 26;

int N;
int char2int[SIZE];

struct compare{
    bool operator()(const int& a, const int& b) {
        return a > b;
    }
};

int main(void) {
    cin >> N;

    for (int i = 0; i < N; i++) {
        string s; cin >> s;

        for (int i = 0; i < s.size(); i++) {
            char &c = s[i];
            char2int[c - 'A'] += pow(10, s.size()-1-i);
        }
    }

    sort(char2int, char2int + SIZE, compare());
    
    int _sum = 0;
    for (int i = 0; i < 10; i++) {
        _sum += char2int[i] * (9 - i);
    }
    printf("%d\n", _sum);
    
    return 0;
}