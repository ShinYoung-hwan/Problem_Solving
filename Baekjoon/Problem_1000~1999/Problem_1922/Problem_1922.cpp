#include <cstdio>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

void _union(vector<int> &parents, const int x, const int y) {
    if (x > y) {
        parents[x] = y;
    } else {
        parents[y] = x;
    }
}

int _find(vector<int> &parents, const int x) {
    if (parents[x] != x) parents[x] = _find(parents, parents[x]);
    return parents[x];
}

int kruskal(const vector<tuple<int, int, int> > &edges, const int V) {
    /* 크루스칼 알고리즘 O(ElogE) */
    vector<int> parents(V+1);
    for(int i = 1; i < V+1; i++) parents[i] = i;
    int cost = 0;

    for (auto edge: edges) {
        int u, v, c;
        tie(c, u, v) = edge;

        int u_root = _find(parents, u);
        int v_root = _find(parents, v);
        if (u_root == v_root) continue;

        _union(parents, u_root, v_root);
        cost += c;
    }

    return cost;
}

int main() {
    int N, M; scanf("%d %d", &N, &M);
    vector<tuple<int, int, int> > edges;
    for (int i = 0; i < M; i++) {
        int a, b, c; scanf("%d %d %d", &a, &b, &c);
        edges.push_back({ c, a, b });
    }
    sort(edges.begin(), edges.end());

    printf("%d\n", kruskal(edges, N));

    return 0;
}