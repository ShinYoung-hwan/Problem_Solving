#include <cstdio>
#include <vector>

using namespace std;

bool visited[10] = { false, };
int cnt = 0;

inline int getMinVisited() {
    for (int i = 0; i < 10; i++) {
        if (!visited[i]) return i;
    }
    return 11;
        
}

void search(const vector<vector<int> > &graph, const int me, const int toPick) {
    // base
    if (!toPick) {
        cnt++;
        return;
    }

    // default
    visited[me] = true;
    for (int myFriend: graph[me]) {
        if (visited[myFriend]) continue;

        visited[myFriend] = true;

        search(graph, getMinVisited(), toPick-1);

        visited[myFriend] = false;
    }
    visited[me] =false;
}

int main(int argc, char **argv) {
    int C; scanf("%d", &C);

    for (int t = 0; t < C; t++) {
        int n, m; scanf("%d %d", &n, &m);
        vector<vector<int> > graph(n);
        for (int i = 0; i < m; i++) {
            int u, v; scanf("%d %d", &u, &v);
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        cnt = 0;
        search(graph, 0, n / 2);
        
        printf("%d\n", cnt);
    }

    return 0;
}