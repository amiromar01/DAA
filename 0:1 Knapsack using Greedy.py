def knapsack_01_greedy(items, W):
    # items = [(value, weight)]
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_v = 0
    chosen = []

    for v, w in items:
        if w <= W:
            W -= w
            total_v += v
            chosen.append((v, w))

    return total_v, chosen
 
print(knapsack_01_greedy([(60, 10), (100, 20), (120, 30)], 50))  # Output: (220, [(100, 20), (120, 30)])
