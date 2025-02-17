#include <cstdio>
#include <utility>
#include <algorithm>

using namespace std;
const int MAXN = 100000;

int main() {
    int T; scanf("%d", &T);

    for (int t = 0; t < T; t++) {
        int N; scanf("%d", &N);
        pair<int, int> applicants[MAXN];
        for (int i = 0; i < N; i++) scanf("%d %d", &applicants[i].first, &applicants[i].second);
        sort(applicants, applicants+N);

        int answer = N;
        int min_interview = applicants[0].second;

        for (int i = 1; i < N; i++) {
            if (applicants[i].second > min_interview) answer--;
            else min_interview = applicants[i].second;
        }

        printf("%d\n", answer);
    }

    return 0;
}