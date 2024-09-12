#include <cstdio>
#include <deque>
#include <utility>

enum { N, S };
enum { COUNTERCLOCKWISE=-1, CLOCKWISE=1 };

using namespace std;
deque<int> wheels[4] = { {}, {}, {}, {} };

void move(const int start, const int dir) {
    deque<pair<int, int> > q;
    bool visited[4] = { false };
    q.push_back({ start, dir });

    while (!q.empty()) {
        int cur = q.front().first, dir = q.front().second;
        q.pop_front();
        int left = cur - 1, right = cur + 1;

        if (0 <= left && !visited[left] && wheels[left][2] != wheels[cur][6]) {
            q.push_back({ left, -dir });
        }
        if (right < 4 && !visited[right] && wheels[cur][2] != wheels[right][6]) {
            q.push_back({ right, -dir });
        }

        if (dir == CLOCKWISE) {
            wheels[cur].push_front(wheels[cur].back());
            wheels[cur].pop_back();
        } else {
            wheels[cur].push_back(wheels[cur].front());
            wheels[cur].pop_front();
        }
        visited[cur] = true;
    }
}

int main() {
    for (int i = 0; i < 4; i++) {
        char str[9]; scanf("%s", str);

        for (int j = 0; j < 8; j++) {
            wheels[i].push_back(str[j] == '1' ? 1 : 0);
        }
    }

    int K; scanf("%d", &K);
    for (int t=0; t < K; t++) {
        int i, dir; scanf("%d %d", &i, &dir);

        move(i-1, dir);
    }

    int score = 0;
    score += wheels[0][0] ? 1 : 0;
    score += wheels[1][0] ? 2 : 0;
    score += wheels[2][0] ? 4 : 0;
    score += wheels[3][0] ? 8 : 0;

    printf("%d\n", score);
    
    return 0;
}