import sys

input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    
    pizza_dict = {
        "1/4": 0,
        "1/2": 0,
        "3/4": 0,
    }
    for _ in range(N):
        pizza_dict[input()] += 1
    
    _sum = 0
    # 1/4 + 3/4
    cur_sum = min(pizza_dict["1/4"], pizza_dict["3/4"])
    pizza_dict["1/4"], pizza_dict["3/4"] = pizza_dict["1/4"] - cur_sum, pizza_dict["3/4"] - cur_sum
    _sum += cur_sum
    
    # 1/4 + 1/4 + 1/2
    cur_sum = min(pizza_dict["1/2"], pizza_dict["1/4"] // 2)
    pizza_dict["1/2"], pizza_dict["1/4"] = pizza_dict["1/2"] - cur_sum, pizza_dict["1/4"] - 2*cur_sum
    _sum += cur_sum
    
    # 1/2 + 1/2
    cur_sum = pizza_dict["1/2"] // 2
    pizza_dict["1/2"] %= 2
    _sum += cur_sum
    
    # 1/4 + 1/4 + 1/4 + 1/4
    cur_sum = pizza_dict["1/4"] // 4
    pizza_dict["1/4"] %= 4
    _sum += cur_sum
    
    # 1/4 + 1/2
    cur_sum = min(pizza_dict["1/2"], pizza_dict["1/4"])
    pizza_dict["1/2"], pizza_dict["1/4"] = pizza_dict["1/2"] - cur_sum, pizza_dict["1/4"] - cur_sum
    _sum += cur_sum
    
    # 3/4
    cur_sum = pizza_dict["3/4"]
    pizza_dict["3/4"] = 0
    _sum += cur_sum
    
    # 1/2
    cur_sum = pizza_dict["1/2"] 
    pizza_dict["1/2"] = 0
    _sum += cur_sum
    
    # 1/4
    cur_sum = bool(pizza_dict["1/4"])
    pizza_dict["1/4"] = 0
    _sum += cur_sum
    
    # print(pizza_dict)
    print(_sum)