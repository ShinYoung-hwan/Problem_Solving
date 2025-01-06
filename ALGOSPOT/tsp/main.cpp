#include <cstdio>
#include <cstdint>
#include <algorithm>

using namespace std;

const int MAXN = 10;

int N = MAXN;
int graph[MAXN][MAXN] = { 0, };
bool visited[MAXN] = { false, };
int ans = INT32_MAX;
int to_visit = 0;

void DFS(const int cur=0, const int cost=0) {
    // base
    if (to_visit == 0 && graph[cur][0] != 0) {
        ans = min(ans, cost + graph[cur][0]);
        return;
    }

    // default
    for (int next = 0; next < N; next++) {
        if (visited[next]) continue;
        if (graph[cur][next] == 0) continue;
        if (ans < cost + graph[cur][next]) continue;

        visited[next] = true;
        to_visit--;
        DFS(next, cost + graph[cur][next]);
        to_visit++;
        visited[next] = false;
    }
}

int main(int argc, char **argv) {
    scanf("%d", &N);
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            scanf("%d", &graph[r][c]);
        }
    }

    visited[0] = true;
    to_visit = N-1;

    DFS();
    
    printf("%d\n", ans);


    return 0;
}