#include <cstdio>
#include <queue>

using namespace std;

int main() {
    int N; scanf("%d", &N);
    priority_queue<int> cards; // max heap
    for (int i = 0; i < N; i++) {
        int card; scanf("%d", &card);
        cards.push(-card);
    }

    int cnt = 0;
    while (cards.size() > 1) {
        int card0 = - cards.top(); cards.pop();
        int card1 = - cards.top(); cards.pop();

        int new_card = card0 + card1;
        cnt += new_card;
        cards.push(-new_card);
    }

    printf("%d\n", cnt);

    return 0;
}