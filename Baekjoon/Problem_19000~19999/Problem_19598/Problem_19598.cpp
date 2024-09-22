#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>

using namespace std;

int main() {
    int N; scanf("%d", &N);
    vector<pair<int, int> > schedules;
    for (int i = 0; i < N; i++) {
        int s, e; scanf("%d %d", &s, &e);
        schedules.push_back({ s, e });
    }
    sort(schedules.begin(), schedules.end());

    priority_queue<int, vector<int>, greater<int> > pq;
    int size = 0;
    for (auto schedule: schedules) {
        while (!pq.empty() && pq.top() <= schedule.first) pq.pop();
        pq.push(schedule.second);
        size = max(size, static_cast<int>(pq.size()));
    }
    
    printf("%d\n", size);
    
    return 0;
}