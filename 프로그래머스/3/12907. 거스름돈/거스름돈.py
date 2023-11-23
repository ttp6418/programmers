def solution(n, money):
    dp = [1] + [0] * n
    [dp.__setitem__(i, (dp[i] + dp[i - coin])%1000000007) for coin in money for i in range(coin, n + 1)]
    return dp[n]