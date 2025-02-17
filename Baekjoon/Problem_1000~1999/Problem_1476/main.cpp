#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int E, S, M;

int get_min_dt(const int e, const int s, const int m) {
    vector<int> minv = { 16 - e, 29 - s, 20 - m };

    if (E - e > 0) minv.push_back(E - e);
    if (S - s > 0) minv.push_back(S - s);
    if (M - m > 0) minv.push_back(M - m);

    return *min_element(minv.begin(), minv.end());
}


int main() {
    scanf("%d %d %d", &E, &S, &M);

    int time = 1;
    int e = 1, s = 1, m = 1;
    while (!(E == e && S == s && M == m)) {
        int dt = get_min_dt(e, s, m);

        e = (e + dt > 15 ? (e + dt) % 15 : (e + dt));
        s = (s + dt > 28 ? (s + dt) % 28 : (s + dt));
        m = (m + dt > 19 ? (m + dt) % 19 : (m + dt));

        time += dt;
    }

    printf("%d\n", time);

    return 0;
}