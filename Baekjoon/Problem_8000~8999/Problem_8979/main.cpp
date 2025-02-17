#include <cstdio>
#include <vector>
#include <tuple>
#include <map>
#include <algorithm>

using namespace std;

bool compare_medals(const tuple<int, int, int, int> &a, const tuple<int, int, int, int> &b) {
    return tie(get<1>(a), get<2>(a), get<3>(a)) > tie(get<1>(b), get<2>(b), get<3>(b));
}
bool equals(const tuple<int, int, int, int> &a, const tuple<int, int, int, int> &b) {
    return tie(get<1>(a), get<2>(a), get<3>(a)) == tie(get<1>(b), get<2>(b), get<3>(b));
}

int main() {
    int N, K; scanf("%d %d", &N, &K);
    vector<tuple<int, int, int, int>> scores;
    for (int i = 0; i < N; i++) {
        int id, gold, silver, copper; scanf("%d %d %d %d", &id, &gold, &silver, &copper);
        scores.push_back({ id, gold, silver, copper });
    }

    sort(scores.begin(), scores.end(), compare_medals);

    map<int, int> score_map;
    tuple<int, int, int, int> prev_tuple = {0, 1000001, 1000001, 1000001};
    for (int i = 0; i < N; i++) {
        tuple<int, int, int, int> &score = scores[i];

        if (!equals(prev_tuple, score)) {
            prev_tuple = score;
            get<0>(prev_tuple) = i;
        }

        score_map.insert({get<0>(score), get<0>(prev_tuple)+1});
    }

    printf("%d\n", score_map[K]);

    return 0;
}