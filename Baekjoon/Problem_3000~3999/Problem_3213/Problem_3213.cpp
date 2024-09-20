#include <cstdio>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    int N; scanf("%d", &N);

    map<string, int> pizza_map = {
        { "1/4", 0 },
        { "1/2", 0 },
        { "3/4", 0 },
    };
    for (int i = 0; i < N; i++) {
        char amount[4]; scanf("%s", amount);
        pizza_map[string(amount)] += 1;
    }

    int _sum = 0;
    // 1/4 + 3/4
    int cur_sum = min(pizza_map["1/4"], pizza_map["3/4"]);
    pizza_map["1/4"] -= cur_sum;
    pizza_map["3/4"] -= cur_sum;
    _sum += cur_sum;

    // 1/4 + 1/4 + 1/2
    cur_sum = min(pizza_map["1/4"]/2, pizza_map["1/2"]);
    pizza_map["1/4"] -= 2*cur_sum;
    pizza_map["1/2"] -= cur_sum;
    _sum += cur_sum;

    // 1/2 + 1/2
    cur_sum = pizza_map["1/2"] / 2;
    pizza_map["1/2"] -= 2*cur_sum;
    _sum += cur_sum;

    // 1/4 + 1/4 + 1/4 + 1/4
    cur_sum = pizza_map["1/4"] / 4;
    pizza_map["1/4"] -= 4*cur_sum;
    _sum += cur_sum;

    // 1/4 + 1/2
    cur_sum = min(pizza_map["1/4"], pizza_map["1/2"]);
    pizza_map["1/4"] -= cur_sum;
    pizza_map["1/2"] -= cur_sum;
    _sum += cur_sum;

    // rest 3/4
    cur_sum = pizza_map["3/4"];
    pizza_map["3/4"] = 0;
    _sum += cur_sum;

    // rest 1/2
    cur_sum = pizza_map["1/2"];
    pizza_map["1/2"] = 0;
    _sum += cur_sum;

    // rest 1/4
    cur_sum = static_cast<bool>(pizza_map["1/4"]);
    pizza_map["1/4"] = 0;
    _sum += cur_sum;

    printf("%d\n", _sum);
    
    return 0;
}