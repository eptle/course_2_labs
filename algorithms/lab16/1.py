def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    print(*dp, sep='\n')
    return dp[n][capacity]


if __name__ == '__main__':
    weights = [0, 3, 0, 5]
    values = [2, 4, 5, 6]
    capacity = 12
    print(knapsack(weights, values, capacity))