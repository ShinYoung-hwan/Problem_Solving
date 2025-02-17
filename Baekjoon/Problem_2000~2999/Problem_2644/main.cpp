#include <cstdio>
#include <vector>
#include <queue>

const int MAXN = 100;

using namespace std;

int N;

int BFS(const vector<vector<int> > &graph, const int s, const int e) {
    queue<int> q;
    int visited[MAXN+1];
    fill(visited, visited + MAXN+1, -1);
    q.push(s);
    visited[s] = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int next: graph[cur]) {
            if (visited[next] >= 0) continue;

            q.push(next);
            visited[next] = visited[cur] + 1;
            if (next == e) return visited[e];
        }
    }

    return visited[e];
}

int main() {
    scanf("%d", &N);
    int s, e; scanf("%d %d", &s, &e);

    int m; scanf("%d", &m);
    vector<vector<int> > graph(static_cast<size_t>(N+1));

    for (int i = 0; i < m; i++) {
        int u, v; scanf("%d %d", &u, &v);
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    printf("%d\n", BFS(graph, s, e));

    return 0;
}